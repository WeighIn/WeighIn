package com.weighin.api.models;

/**
 * Created by Dylan on 9/24/2014.
 */
class task extends _base {

    private final String _name;
    private final application _app;
    private final long _worth; // Points
    private final String _data; // HTML?

    public String getName() { return _name; }
    public application getApp() { return _app; }
    public long getWorth() { return _worth; }
    public String getData() { return _data; }

    public task(String name, application app, long worth, String data) {
        _name = name;
        _app = app;
        _worth = worth;
        _data = data;
    }
}
