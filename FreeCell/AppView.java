import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;

 /**
 *  A <code>AppView </code> will handel the visual representation of the game of free cell.
 *  It will display the cards, the status of the game, and allow users to make moves
 *  as they please and reset the game whenever they want to.
 *  @author Bryce Burnette
 *  @author Ana Estrada
 *  @author Evan Phaup
 *  file: AppView.java
 *  Handles the visual representation of the game.
 */
public class AppView extends JFrame{

    private GameModel game;
    private JLabel freeCellsLabel = new JLabel("Free Cells", SwingConstants.CENTER);
    private JLabel homeCellsLabel = new JLabel("Home Cells", SwingConstants.CENTER);
    private JLabel numGamesLabel = new JLabel("Game: 1", SwingConstants.CENTER);
    private JLabel numWinsLabel = new JLabel("Wins: 0", SwingConstants.CENTER);
    private JLabel numLossesLabel = new JLabel("Losses: 0", SwingConstants.CENTER);
    private JLabel numMovesLabel = new JLabel("Moves: 0", SwingConstants.CENTER);
    private int numGames = 1;
    private int numWins = 0;
    private int numLosses = 0;
    private int numMoves = 0;
    private Color darkGreen = new Color(0, 102, 0);
    private ArrayList<MultiCardPanel> tableaus = new ArrayList<MultiCardPanel>();
    private ArrayList<SingleCardPanel> homeCells = new ArrayList<SingleCardPanel>();
    private ArrayList<SingleCardPanel> freeCells = new ArrayList<SingleCardPanel>();
    private JButton gameButton = new JButton("New Game");
    private boolean bool;
    private CellPanel panel1 = null;
    private CellPanel panel2 = null;
    private boolean firstCard = false;

    /**
     * Sets up the GUI view of the game
     * @param game the game model to be used
     */
    public AppView(GameModel game){

        this.game = game;
        this.setTitle("The Game of Free Cell");
        for (int i = 0; i<=7; i++)
        {
            tableaus.add(new MultiCardPanel(game.useTableaus().get(i)));
        }
        for (int i = 0; i <=3; i++)
        {
            freeCells.add(new SingleCardPanel(game.useFreeCells().get(i)));
            homeCells.add(new SingleCardPanel(game.useHomeCells().get(i)));
        }

        for (int i = 0; i<=7; i++)
        {
          tableaus.get(i).addMouseListener(new Clicker(tableaus.get(i)));
        }

        for (int i = 0; i <=3; i++)
        {
          freeCells.get(i).addMouseListener(new Clicker(freeCells.get(i)));
        }

        for (int i = 0; i <=3; i++)
        {
          homeCells.get(i).addMouseListener(new Clicker(homeCells.get(i)));
        }

        Container c = getContentPane();
          JPanel topPanel = new JPanel();
            topPanel.setLayout(new GridLayout(2,1));
            JPanel labelPanel = new JPanel();
              labelPanel.setLayout(new GridLayout(1, 2));
              labelPanel.setBackground(Color.black);
              freeCellsLabel.setForeground(Color.white);
              homeCellsLabel.setForeground(Color.white);
              labelPanel.add(freeCellsLabel);
              labelPanel.add(homeCellsLabel);
            JPanel infoPanel = new JPanel();
              infoPanel.setLayout(new GridLayout(1, 4));
              infoPanel.setBackground(darkGreen);
              numGamesLabel.setForeground(Color.white);
              numWinsLabel.setForeground(Color.yellow);
              numLossesLabel.setForeground(Color.red);
              numMovesLabel.setForeground(Color.white);
              infoPanel.add(numGamesLabel);
              infoPanel.add(numWinsLabel);
              infoPanel.add(numLossesLabel);
              infoPanel.add(numMovesLabel);
            topPanel.add(labelPanel);
            topPanel.add(infoPanel);
          JPanel gamePanel = new JPanel();
            gamePanel.setBackground(darkGreen);
            gamePanel.setOpaque(true);
            gamePanel.setLayout(new GridBagLayout());
            GridBagConstraints gbc = new GridBagConstraints();
            int x = 0; int y = 0;
            gbc.ipadx = 72; gbc.ipady = 100;
            for (int i = 0; i <= 3; i++){
              gbc.fill = GridBagConstraints.HORIZONTAL;
              gbc.weightx = .5;
              gbc.gridx = x; gbc.gridy = y;
              gamePanel.add(freeCells.get(i), gbc);
              x++;
            }
            for (int i = 0; i <= 3; i++){
              gbc.fill = GridBagConstraints.HORIZONTAL;
              gbc.weightx = .5;
              gbc.weighty = .5;
              gbc.gridx = x; gbc.gridy = y;
              homeCells.get(i).setFrameColor(true);
              gamePanel.add(homeCells.get(i), gbc);
              x++;
            }
            x = 0; y = 1;
            gbc.ipady = 500;
            for (int i = 0; i <= 7; i++){
              gbc.fill = GridBagConstraints.HORIZONTAL;
              gbc.weightx = .5;
              gbc.weighty = 1;
              gbc.gridx = x; gbc.gridy = y;
              gamePanel.add(tableaus.get(i), gbc);
              x++;
            }
              gameButton.addActionListener(new ActionListener(){
                  public void actionPerformed(ActionEvent e){
                      game.newGame();
                      numGames++;
                      numLosses++;
                      numMoves = 0;
                      firstCard = false;
                      numLossesLabel.setText("Losses: " + numLosses);
                      numMovesLabel.setText("Moves: " + numMoves);
                      numGamesLabel.setText("Game: " + numGames);
                      repaint();
                    }
                });
          JPanel buttonPanel = new JPanel();
            buttonPanel.setLayout(new GridBagLayout());
            GridBagConstraints bpc = new GridBagConstraints();
            bpc.fill = GridBagConstraints.VERTICAL;
            bpc.ipadx = 36;
            bpc.gridx = 0; bpc.gridy = 0;
            buttonPanel.setBackground(Color.black);
            gameButton.setBackground(Color.white);
            buttonPanel.add(gameButton, bpc);
          c.add(topPanel, BorderLayout.NORTH);
          c.add(gamePanel, BorderLayout.CENTER);
          c.add(buttonPanel, BorderLayout.SOUTH);
    }

    /**
     * class that handles the event of a mouse click
     */
    public class Clicker extends MouseAdapter{

      private CellPanel cell = null;
      int n = -1;

      public Clicker(CellPanel cellPanel)
      {
        cell = cellPanel;
      }

      public void mouseClicked(MouseEvent e){
        //System.out.println("Yo");
        //System.out.println("panel1= "+panel1);
        //System.out.println("panel2= "+panel2);
        if (firstCard == false)
        {
          panel1 = cell;
          firstCard = true;
        }

        else
        {
          numMoves +=1;
          numMovesLabel.setText("Moves: " + numMoves);
          panel2 = cell;
          if(panel1 == panel2){
            JOptionPane.showMessageDialog(new JFrame(), "You clicked the same card twice!", "Wrong Move", JOptionPane.WARNING_MESSAGE);
          }
          else if(!game.move(panel1.getCell(), panel2.getCell())){

            //need to update the number of moves here
            JOptionPane.showMessageDialog(new JFrame(), "Illegal move", "Wrong Move", JOptionPane.WARNING_MESSAGE);
          }
          else{
            firstCard = false;
            repaint();
          }
        firstCard = false;
        }
        if(!(game.canMove()) && !(game.gameOver())){
          n = JOptionPane.showConfirmDialog(new JFrame(), "You Lost! Would you like to play another game?", "Loser!", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
          numWins += 1;
          numLosses += 1;
          System.out.println(n);
          numLossesLabel.setText("Losses: " + numLosses);
        }
        else if(game.gameOver()){
          n = JOptionPane.showConfirmDialog(new JFrame(), "You Won! Would you like to play another game?", "Winner!", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
          numWins += 1;
          numWinsLabel.setText("Wins: " + numWins);
        }
        if (n == 0){
          game.newGame();
          numGames++;
          n= -1;
          numMoves = 0;
          firstCard = false;
          numMovesLabel.setText("Moves: " + numMoves);
          numGamesLabel.setText("Game: " + numGames);
          repaint();
        }
      }
    }
  }
