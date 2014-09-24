package com.weighin.api.models;

import java.util.Map;

/**
 * Created by Dylan on 9/24/2014.
 */
public class _base {

    private Map<String,String> _attributes;

    public Map<String,String> getAttributes() { return _attributes; }
    public String getAttribute(String name) { return _attributes.getOrDefault(name, null); }

    public void setAttributes(Map<String,String> attributes) { this._attributes = attributes; }
    public void setAttribute(String name, String value) { _attributes.put(name, value); }
}
