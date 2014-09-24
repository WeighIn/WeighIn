package com.weighin.api.models;

import java.security.MessageDigest;

/**
 * Created by Dylan on 9/19/2014.
 */
public class user extends _base {

    private String _username;
    private String _email;
    private String _password_hash;

    public String getUsername() { return _username; }
    public String getEmail() { return _email; }
    public String getPasswordHash() { return _password_hash; }

    public void setUsername(String username) { this._username = username; }
    public void setEmail(String email) throws Exception { this._email = verifyEmail(email); }
    public void setPassword(String password) throws Exception { this._password_hash = hashPassword(password); }
    public void setPasswordHash(String password_hash) { this._password_hash = password_hash; }

    public boolean checkPassword(String password) throws Exception {
        return this._password_hash == hashPassword(password);
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
}
