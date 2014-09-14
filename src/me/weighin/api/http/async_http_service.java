package me.weighin.api.http;

import java.io.PrintStream;
import java.net.InetSocketAddress;
import java.net.SocketAddress;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.SynchronousQueue;

import org.simpleframework.http.Request;
import org.simpleframework.http.Response;
import org.simpleframework.http.core.Container;
import org.simpleframework.http.core.ContainerServer;
import org.simpleframework.transport.Server;
import org.simpleframework.transport.connect.Connection;
import org.simpleframework.transport.connect.SocketConnection;

/**
 * Created by Dylan on 9/13/2014.
 */
public class async_http_service implements Container {

    public static class Task implements Runnable {

        private final Response response;
        private final Request request;

        public Task(Request request, Response response) {
            this.response = response;
            this.request = request;
        }

        public void run() {
            // Runnable code
        }
    }

    private final Executor executor;

    public async_http_service(int minThreads, int maxThreads, long threadKeepAlive) {
        this.executor = new ThreadPoolExecutor(minThreads, maxThreads,
                threadKeepAlive, TimeUnit.SECONDS, new SynchronousQueue<Runnable>());
    }

    public void handle(Request request, Response response) {
        Task task = new Task(request, response);
        executor.execute(task);
    }
}
