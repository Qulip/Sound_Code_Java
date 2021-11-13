package com.example.soundCode.domain;

import com.example.soundCode.domain.util.RestApi;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;


@RestController
public class PythonModelApi {

    private final RestApi restApi;

    public PythonModelApi(RestApi restApi) {
        this.restApi = restApi;
    }

    @GetMapping("test")
    public String test(@RequestParam("name") String name) throws UnsupportedEncodingException {
        String names = URLEncoder.encode(name, "UTF-8");
        System.out.println("이거 뭐임?");
        String temp = restApi.get("http://localhost:5000/test/" + names);
        StringBuilder sb = new StringBuilder(temp);
        System.out.println("temp = " + temp);
        sb.deleteCharAt(0);
        sb.deleteCharAt(sb.length() - 2);

        System.out.println("sb.toString() = " + sb.toString());

        String[] split = sb.toString().split(",");


        return split[0];
    }

    @PostMapping("test")
    public String test2(@RequestParam("wav") MultipartFile file) throws IOException {

        String filePath = "D:\\코딩\\개발코드\\졸프음성\\2semester\\data\\" + "chang" + ".wav";
        File dest = new File(filePath);
        file.transferTo(dest);

        return "Success";
    }


}
