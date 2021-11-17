package com.example.soundCode.domain;

import lombok.Getter;

@Getter
public class CodeDto {
    String key;

    public CodeDto(String key) {
        this.key = key;
    }
}
