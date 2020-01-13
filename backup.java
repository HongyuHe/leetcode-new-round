package tech.picnic.assignment.impl;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonIOException;
import com.google.gson.JsonSyntaxException;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonToken;
import tech.picnic.assignment.api.StreamProcessor;
import tech.picnic.assignment.impl.inputevent.PickEvent;
import tech.picnic.assignment.impl.outputlog.ArticleLog;
import tech.picnic.assignment.impl.outputlog.PickerLog;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Collectors;

public class PickingStreamProcessor implements StreamProcessor {

    private OutputStream sink;
    private InputStream source;
    private int maxEvents;
    private Duration maxTime;
    private int processedEvents;
    private AtomicBoolean isReadfinsh = new AtomicBoolean(false);
    private List<PickEvent> pendingEvents = new ArrayList<>();
    private ExecutorService executor = Executors.newFixedThreadPool(3);
    private BlockingQueue<PickEvent> eventBlockingQueue = new LinkedBlockingDeque<>();

    private Gson gson = (new GsonBuilder().setPrettyPrinting().excludeFieldsWithoutExposeAnnotation()).create();

    private Thread readThread = new Thread(this::readEventsFromSource);
    private Thread addThread = new Thread(this::addEventsToPendingQueue);
    private Thread timer = new Thread(this::timer);

    PickingStreamProcessor(int maxEvents, Duration maxTime) {
        this.maxEvents = maxEvents;
        this.maxTime = maxTime;
        processedEvents = 0;
    }

    @Override
    public void process(InputStream source, OutputStream sink) throws IOException {
        this.source = source;
        this.sink = sink;
        // Future<?> readThread = executor.submit(this::readEventsFromSource);
        // Future<?> addThread = executor.submit(this::addEventsToPendingQueue);

        try {
            // readThread.get(maxTime.getSeconds(), TimeUnit.SECONDS);
            // addThread.get(maxTime.getSeconds(), TimeUnit.SECONDS);

            // executor.execute(this::readEventsFromSource);
            // executor.execute(this::addEventsToPendingQueue);
            // executor.execute(this::timer);
            //
            // while(!isTimeOut.get()) {
            // if (processedEvents > maxEvents)
            // break;
            // }
            // executor.shutdownNow();
            // addThread.start();
            // timer.start();

            // addThread.join();
            readThread.start();
            readThread.join();
            // timer.join();
            // wait();
            // String log = gson.toJson(producePickerLogsFromPendingEvents());
            //// System.out.println(log);
            // sink.write(log.getBytes(String.valueOf(StandardCharsets.UTF_8)));
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }

    @Override
    public void close() {
        // executor.shutdown();
        try {
            // executor.awaitTermination(1, TimeUnit.SECONDS);
            String log = gson.toJson(producePickerLogsFromPendingEvents());
            // System.out.println(log);
            sink.write(log.getBytes(String.valueOf(StandardCharsets.UTF_8)));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void readEventsFromSource() {
        JsonReader reader = new JsonReader(new InputStreamReader(source, StandardCharsets.UTF_8));
        reader.setLenient(true);
        try {
            while (reader.hasNext() && processedEvents < maxEvents) {
                JsonToken nextToken = reader.peek();
                if (JsonToken.BEGIN_OBJECT.equals(nextToken)) {
                    // assume there is always a whole package
                    processedEvents++;
                    PickEvent pickEvent = gson.fromJson(reader, PickEvent.class);
                    // System.out.println("Offer >>> " + pickEvent);
                    if (pickEvent.getArticle().getTemperatureZone().equals("ambient"))
                        pendingEvents.add(pickEvent);
                    // eventBlockingQueue.offer(pickEvent);
                } else if (Thread.interrupted() || JsonToken.END_DOCUMENT.equals(nextToken)) {
                    break;
                }
                // isReadfinsh.set(true);
                // addThread.wait();
                // timer.interrupt();
                // addThread.interrupt();
            }
        } catch (JsonIOException | JsonSyntaxException | IOException e) {
            e.printStackTrace();
        }
    }

    private void addEventsToPendingQueue() {
        try {
            while (!isReadfinsh.get() || !eventBlockingQueue.isEmpty()) {
                PickEvent event = eventBlockingQueue.take();
                System.out.println("Take >>> " + event);
                pendingEvents.add(event);
            }
        } catch (InterruptedException e) {
            // throw new InterruptedException();
            // e.printStackTrace();
        }
    }

    private void timer() {
        try {
            // Thread.sleep(maxTime.toMillisPart());
            Thread.sleep(1000);
            readThread.interrupt();
            addThread.interrupt();
            // isTimeOut.set(true);
        } catch (InterruptedException e) {
            // e.printStackTrace();
        }
    }

    private List<PickerLog> producePickerLogsFromPendingEvents() {
        // filter on `ambient`
        List<PickEvent> filteredEvents = pendingEvents.stream()
                .filter(pickEvent -> pickEvent.getArticle().getTemperatureZone().equals("ambient"))
                .collect(Collectors.toList());

        Map<String, PickerLog> logMap = new HashMap<>();
        for (PickEvent event : filteredEvents) {

            logMap.putIfAbsent(event.getPicker().getId(), new PickerLog(event.getPicker().getId(),
                    event.getPicker().getName(), event.getPicker().getActiveSince()));

            logMap.get(event.getPicker().getId()).getPicks().add(new ArticleLog(event.getArticle().getId(),
                    event.getArticle().getName().toUpperCase(), event.getTimeStamp()));
        }

        /*
         * @link <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601
         * lexicographical order </a>
         */
        List<PickerLog> pickerLogs = new ArrayList<>(logMap.values());
        pickerLogs.sort(Comparator.comparing(PickerLog::getActiveSince).thenComparing(PickerLog::getId));
        pickerLogs.forEach(pickerLog -> pickerLog.getPicks()
                .sort(Comparator.comparing(ArticleLog::getTimeStamp).thenComparing(ArticleLog::getId)));

        return pickerLogs;
    }

}
