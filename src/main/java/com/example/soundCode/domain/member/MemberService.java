package com.example.soundCode.domain.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MemberService {

    @Autowired
    MemberRepository memberRepository;

    public void save(Member member) {
        memberRepository.save(member);
    }

    public void save(String loginId, String loginPw, String name, String phoneNumber) {
        Member member = new Member(loginId, loginPw, name, phoneNumber);
        memberRepository.save(member);
    }

    public boolean login(String id, String pwd) {
        Member member = memberRepository.findByLoginId(id);
        if (member == null) {
            System.out.println("없음!");
        }

        return member.getPassword().equals(pwd);
    }
}
