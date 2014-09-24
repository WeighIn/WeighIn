package com.weighin.api.models;

import java.security.MessageDigest;

/**
 * Created by Dylan on 9/19/2014.
 */
public class user extends _base {

    private String username;
    private String email;
    private String password;

    public String getUsername() { return username; }
    public String getEmail() { return email; }
    public String getPasswordHash() { return password; }

    public void setUsername(String username) { // TODO: Check for uniqueness
        this.username = username;
    }

    public void setEmail(String email) throws Exception { // TODO: Check for uniqueness
        this.email = verifyEmail(email);
    }

    public void setPassword(String password) throws Exception { this.password = hashPassword(password); }
    public void setPasswordHash(String password_hash) { this.password = password_hash; }

    public boolean checkPassword(String password) throws Exception {
        return this.password == hashPassword(password);
    }

    private String hashPassword(String password) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(password.getBytes("UTF-8"));
        return new String(md.digest(), "UTF-8");
    }

    private String verifyEmail(String email) throws Exception {
        if (!com.weighin.api.models.email.verify(email)) throw new Exception("Email address format isn't valid");
        // Do any email manipulation
        return email;
    }

    public user(String username, String email, String password) throws Exception {
        setUsername(username);
        setEmail(email);
        setPassword(password);
    }
}
