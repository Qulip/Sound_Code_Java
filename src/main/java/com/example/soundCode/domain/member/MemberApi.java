package com.example.soundCode.domain.member;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

@Controller
public class MemberApi {

    private final MemberService memberService;

    public MemberApi(MemberService memberService) {
        this.memberService = memberService;
    }

    @PostMapping("register")
    public String register(HttpServletRequest httpServletRequest, Model model) {
        String loginId = httpServletRequest.getParameter("loginId");
        String loginPw = httpServletRequest.getParameter("loginPw");
        String loginPwConfirm = httpServletRequest.getParameter("loginPwConfirm");
        String name = httpServletRequest.getParameter("name");
        String phoneNumber = httpServletRequest.getParameter("phoneNumber");

        if (loginPw.equals(loginPwConfirm)) {
            memberService.save(loginId, loginPw, name, phoneNumber);
            model.addAttribute("status", "success");
            return "test";
        }

        model.addAttribute("status", "fail");
        return "test";
    }


    @PostMapping("login")
    public String test(HttpServletRequest httpServletRequest, HttpSession httpSession, Model model) {
        String id = httpServletRequest.getParameter("loginId");
        String pwd = httpServletRequest.getParameter("loginPw");
        model.addAttribute("userId", id);
        if (memberService.login(id, pwd)) {
            httpSession.setAttribute("userId", id);
            return "test";
        }

        return "login";
    }
}
