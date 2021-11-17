package com.example.soundCode.domain;

import lombok.Getter;

@Getter
public class AuthenticateDto {
    String pass;
    String recognize;
    String stt;

    public AuthenticateDto(String  pass, String recognize, String stt) {
        this.pass = pass;
        this.recognize = recognize;
        this.stt = stt;
    }
}
