/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package bclient;

/**
 *
 * @author sebbz
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        MainWindow a = new MainWindow();
        a.setVisible(true);
        IrcConnection k = new IrcConnection();
        k.connect();
    }

}
