import javax.swing.JFrame;

/**java
 * Generic main method template for any GUI-based application.
 * Instantiates a model and passes it to a new view.
 * @author lambertk
 * file: FreeCellApp.java
 */
public class FreeCellApp{
    public static void main(String[] args){
        final GameModel game = new GameModel();
        final JFrame view = new AppView(game);
        view.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        view.setSize(800, 800);
        view.setVisible(true);
    }
}
