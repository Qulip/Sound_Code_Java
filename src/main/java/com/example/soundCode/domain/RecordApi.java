package com.example.soundCode.domain;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;

@RestController
public class RecordApi {


    @PostMapping("register/record")
    public String registerRecord(@RequestParam("wav") MultipartFile file) throws IOException {
        String filePath = "D:\\코딩\\자바\\soundCode\\python_server\\data\\" + "register" + ".wav";
        File dest = new File(filePath);
        file.transferTo(dest);

        return "Success";
    }

    @PostMapping("security/record")
    public String securityRecord(@RequestParam("wav") MultipartFile file) throws IOException {
        String filePath = "D:\\코딩\\자바\\soundCode\\python_server\\data\\" + "security" + ".wav";
        File dest = new File(filePath);
        file.transferTo(dest);

        return "Success";
    }
}
