package com.weighin.api.models;

import java.util.*;
import java.security.MessageDigest;

/**
 * Created by Dylan on 9/19/2014.
 */
public class user {

    private String username;
    private String email;
    private String password_hash;
    private Map<String,String> attributes;

    public String getUsername() { return username; };
    public String getEmail() { return username; };
    public String getPasswordHash() { return username; };
    public Map<String,String> getAttributes() { return attributes; };
    public String getAttribute(String name) { return attributes.getOrDefault(name, null); };

    public void setUsername(String username) { this.username = username; };
    public void setEmail(String email) { this.email = email; };
    public void setPasswordHash(String password_hash) { this.password_hash = password_hash; };
    public void setAttributes(Map<String,String> attributes) { this.attributes = attributes; };

    private String hashPassword(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(password.getBytes("UTF-8"));
        return new String(md.digest(), "UTF-8");
    };

    public void setPassword(String password) throws Exception {
        this.password_hash = hashPassword(password);
    };

    public boolean checkPassword(String password) throws Exception {
        return this.password_hash == hashPassword(password);
    };
}
