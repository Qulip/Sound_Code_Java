package com.example.soundCode.domain;

import com.example.soundCode.domain.util.RestApi;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
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
    public ResponseEntity<Dto> test(@RequestParam("name") String name) throws UnsupportedEncodingException {
        String names = URLEncoder.encode(name, "UTF-8");
        System.out.println("names = " + names);
        String temp = restApi.get("http://localhost:5000/test/" + names);
        StringBuilder sb = new StringBuilder(temp.replace("\n", "").replace(" ", ""));

        System.out.println("temp = " + temp);
        sb.deleteCharAt(0);
        sb.deleteCharAt(sb.length() - 2);
        System.out.println("sb.toString() = " + sb.toString());

        String[] split = sb.toString().split(",");
        for (String s : split) {
            System.out.println("s = " + s);
        }
        Dto dto = new Dto(split[0], split[1], split[2].replace("]",""));

        return ResponseEntity.status(HttpStatus.OK).body(dto);
    }

    @PostMapping("test")
    public String test2(@RequestParam("wav") MultipartFile file) throws IOException {
//D:\코딩\자바\soundCode\python_server\data
        String filePath = "D:\\코딩\\자바\\soundCode\\python_server\\data\\" + "chang" + ".wav";
        File dest = new File(filePath);
        file.transferTo(dest);

        return "Success";
    }


}
