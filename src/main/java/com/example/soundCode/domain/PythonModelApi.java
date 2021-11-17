package com.example.soundCode.domain;

import com.example.soundCode.domain.util.RestApi;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Arrays;
import java.util.List;


@RestController
public class PythonModelApi {

    private final RestApi restApi;
    private static final List<String> keySet = Arrays.asList("안녕하세요 2차 인증 테스트 입니다",
            "파이썬과 자바",
            "애플과 갤럭시",
            "노트북 컴퓨터 키보드 마우스",
            "책상에서 공부하는 학생");
    public PythonModelApi(RestApi restApi) {
        this.restApi = restApi;
    }

    @GetMapping("authenticate")
    public ResponseEntity<AuthenticateDto> authenticate(@RequestParam("name") String name) throws UnsupportedEncodingException {
        String names = URLEncoder.encode(name, "UTF-8");
        System.out.println("names = " + names);
        String temp = restApi.get("http://localhost:5000/authenticate/" + names);
        StringBuilder sb = new StringBuilder(temp.replace("\n", "").replace(" ", ""));

        System.out.println("temp = " + temp);
        sb.deleteCharAt(0);
        sb.deleteCharAt(sb.length() - 2);
        System.out.println("sb.toString() = " + sb.toString());

        String[] split = sb.toString().split(",");
        for (String s : split) {
            System.out.println("s = " + s);
        }
        AuthenticateDto authenticateDto = new AuthenticateDto(split[0], split[1], split[2].replace("]",""));

        return ResponseEntity.status(HttpStatus.OK).body(authenticateDto);
    }

    @GetMapping("getKey")
    public ResponseEntity<CodeDto> getKey() throws UnsupportedEncodingException {
        String response = restApi.get("http://localhost:5000/getKey").replace("\n", "");

        int keyIndex = Integer.parseInt(response);
        String key = keySet.get(keyIndex);
        CodeDto codeDto = new CodeDto(key);
        return ResponseEntity.status(HttpStatus.OK).body(codeDto);
    }

}
