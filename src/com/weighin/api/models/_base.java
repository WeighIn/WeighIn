package com.weighin.api.models;

import java.util.Map;

/**
 * Created by Dylan on 9/24/2014.
 */
class _base {

    private Map<String,String> attributes;

    public Map<String,String> getAttributes() { return attributes; }
    public String getAttribute(String name) { return attributes.getOrDefault(name, null); }

    public void setAttributes(Map<String,String> attributes) { this.attributes = attributes; }
    public void setAttribute(String name, String value) { attributes.put(name, value); }
}
