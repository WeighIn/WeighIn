package com.weighin.api.models;

/**
 * Created by Dylan on 9/24/2014.
 */
public class task extends _base {

    private final String name;
    private final application app;
    private final long worth; // Points
    private final String data; // HTML

    public String getName() { return name; }
    public application getApp() { return app; }
    public long getWorth() { return worth; }
    public String getData() { return data; }

    public task(String name, application app, long worth, String data) {
        this.name = name;
        this.app = app;
        this.worth = worth;
        this.data = data;
    }
}
