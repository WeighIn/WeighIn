package com.weighin.api.models;

import com.fasterxml.jackson.annotation.*;

/**
 * Created by Dylan on 9/19/2014.
 */
public class attribute {

    private String name;
    private String value;

    public String getName() { return name; };
    public String getValue() { return value; };

    public void setName(String name) { this.name = name; };
    public void setValue(String value) { this.value = value; };
}
