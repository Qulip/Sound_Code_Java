package com.example.soundCode;


import org.python.core.PyFunction;
import org.python.core.PyInteger;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@SpringBootTest
public class Test {

    private static PythonInterpreter pythonInterpreter;

    @RequestMapping(value = "test", method = RequestMethod.GET)
    public String getTest() {
        pythonInterpreter = new PythonInterpreter();
        pythonInterpreter.execfile("2semester/main.py");
        pythonInterpreter.exec("print(execute(\"sound_data/0/감자고구마.wav\"))");

        String path = "sound_data/0/감자고구마.wav";
        PyFunction pyFunction = (PyFunction) pythonInterpreter.get("execute", PyFunction.class);
        PyObject pyObject = pyFunction.__call__(new PyString(path));
        System.out.println(pyObject.toString());

        return pyObject.toString();
    }
    @RequestMapping(value = "test2", method = RequestMethod.GET)
    public String getTest2() {
        pythonInterpreter = new PythonInterpreter();
        pythonInterpreter.execfile("2semester/test.py");
        pythonInterpreter.exec("print(testFunc(10,5))");

        PyFunction pyFunction = pythonInterpreter.get("execute", PyFunction.class);
        int a = 30;
        int b = 40;
        PyObject pyObject = pyFunction.__call__(new PyInteger(a), new PyInteger(b));
        System.out.println(pyObject.toString());

        return pyObject.toString();
    }

}
