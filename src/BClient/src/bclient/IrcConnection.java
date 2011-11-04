/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package bclient;
import java.net.*;
import java.io.*;

/**
 *
 * @author kpx
 */
public class IrcConnection {
    private Socket socket;
    private BufferedReader in;
    private PrintWriter out;

    public void connect(){
        try{
        socket = new Socket("irc.se.quakenet.org", 6667);
        out = new PrintWriter(socket.getOutputStream(),
                 true);
        in = new BufferedReader(new InputStreamReader(
                socket.getInputStream()));
        System.out.println(in.readLine());
        out.println("NICK ClientTest");
        System.out.println("Efter nick");
        out.println("USER b-test b-test b-test b-teston");
        System.out.println("Efter user");
        int num = 0;
        String s = "";
        out.flush();
        while ( (s = in.readLine()) != null){
            System.out.println(s);
            if (s.indexOf("004") >= 0)
                    break;
            String[] w = s.split(":");
            System.out.println("InString" + s);
            if (w[0].startsWith("PING")){
                out.println("PONG " + w[1]);
                System.out.println("Loop "+ num);
                num++;
            }
             
        }
        //try {Thread.sleep(3000);}catch (Exception e){}
        out.println("JOIN #b-game");
                System.out.println(in.readLine());
        } catch (UnknownHostException e) {
        System.out.println("Unknown host: kq6py");
        System.exit(1);
        } catch  (IOException e) {
        System.out.println("No I/O");
        System.exit(1);
    }
    }
}
