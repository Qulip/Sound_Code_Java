package com.example.soundCode.domain;

import lombok.Getter;

@Getter
public class Dto {
    String pass;
    String recognize;
    String stt;

    public Dto(String  pass, String recognize, String stt) {
        this.pass = pass;
        this.recognize = recognize;
        this.stt = stt;
    }
}
