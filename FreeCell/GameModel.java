/**
 * A <code>GameModel</code> plays the game of free cell solitaire
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: GameModel.java
 * project5
 * This program creates the game and controls all the rules
 */

import java.util.*;

/**
 * A game model that allows the game to be played
 */
public class GameModel{

    private ArrayList<Tableau> tableaus = new ArrayList<Tableau>();
    private ArrayList<HomeCell> homeCells = new ArrayList<HomeCell>();
    private ArrayList<FreeCell> freeCells = new ArrayList<FreeCell>();
    private Deck deck;

    /**
     * Initializes a game model object
     * Sets up cells
     */
    public GameModel(){

        for(int i=1;i<=8;i++)
        {
            tableaus.add(new Tableau());
        }

        for(int i=1;i<=4;i++)
        {
            homeCells.add(new HomeCell());
        }

        for(int i=1;i<=4;i++)
        {
            freeCells.add(new FreeCell());
        }
        this.deal();
    }

    /**
     * Allows the tableaus to be used
     * @return array list of tableaus
     */
    public ArrayList<Tableau> useTableaus(){
        return tableaus;
    }

    /**
     * Allows home cells to be used
     * @return array list of home cells
     */
    public ArrayList<HomeCell> useHomeCells(){
        return homeCells;
    }

    /**
     * Allows free cells to be used
     * @return array list of free cells
     */
    public ArrayList<FreeCell> useFreeCells(){
        return freeCells;
    }

    /**
     * Deals the cards properly to start the game
     */
    public void deal(){
        deck = new Deck();
        deck.shuffle();

        while (! deck.isEmpty())
        {
            for(int i=0;i<=3;i++)
            {
                for(int x=1;x<=7;x++)
                {
                    tableaus.get(i).add(deck.deal());
                }
            }

            for(int i=4;i<=7;i++)
            {
                for(int x=1;x<=6;x++)
                {
                    tableaus.get(i).add(deck.deal());
                }
            }
        }
    }

    /**
     * 
     * @param cellFrom cell that the card is moving from
     * @param cellTo cell that the card is moving to
     * @return boolean true if and only if the move was valid and successful 
     */
    public boolean move(Cell cellFrom, Cell cellTo)
    {
        if (canMove()){
              if (cellTo.canMoveFrom(cellFrom) && !(cellTo instanceof Tableau && cellTo.isEmpty()) || cellFrom instanceof FreeCell){
                  cellTo.addFrom(cellFrom);
                  return true;
              }

            else if ((cellFrom instanceof Tableau) && (cellTo instanceof Tableau)){

                Tableau tabFrom = (Tableau) cellFrom;
                Tableau tabTo = (Tableau) cellTo;
                for(int i = 0; i< cellFrom.size(); i++){
                    if (tabFrom.isGroupValid(i, tabTo)){
                        tabTo.addGroupCards(tabFrom.getGroupCards(i, tabTo));
                        return true;
                    }

                }
            }

        }
        return false;
    }


    /**
     * Checks to see if the game is over
     * @return true if the game is over
     */
    public boolean gameOver(){
        int x = 0;
        int y = 0;
        for(int i=0;i<=3;i++){
            if (homeCells.get(i).size() == HomeCell.MAX_SIZE)
            {
                x++;
            }
        }
        if (x == 4)
        {
            return true;
        }
        for (Tableau tab: tableaus)
        {
            if (tab.inOrder(0))
            {
                y++;
            }
        }
        if (y == 8)
        {
            return true;
        }
        return false;
    }

    /**
     * Tells if a move can be made
     * @return true if there is a move that can be made
     */
    public boolean canMove(){
        //free cells to tableaus
        //tableaus to tableaus
        //tableaus to freeCells
        int tabToTab = 0;
        int freeToTab = 0;
        int freeCellEmpty = 0;
        int homeCellMoves = 0;
        int tabToFree = 0;

        for(Tableau tab : tableaus)
        {
            for(int i = 0; i<=7; i++)
            {
                if (!(tab.canMoveFrom(tableaus.get(i))))
                {
                    tabToTab++;
                }
            }


            for(int x = 0; x<=3; x++)
            {
                if (!(homeCells.get(x).canMoveFrom(tab)))
                {
                    homeCellMoves++;
                }


            }
            for(int x = 0; x<=3; x++)
            {
                if (!(tab.canMoveFrom(freeCells.get(x))))
                {
                    freeToTab++;
                }


            }
        }
        for(int x = 0; x<=3; x++)
        {
            if (!(freeCells.get(x).isEmpty()))
            {
                tabToFree++;
            }


        }
        for(int x = 0; x<=3; x++)
        {
          for(FreeCell cell: freeCells){
            if (! (homeCells.get(x).canMoveFrom(cell)))
            {
                homeCellMoves++;
            }
          }
      }
        for(FreeCell free : freeCells)
        {
            if (free.isEmpty())
            {
                freeCellEmpty++;
            }
        }

        if (tabToTab == 64 && freeToTab == 32 && tabToFree == 4 && freeCellEmpty == 0 && homeCellMoves == 48)
        {
            return false;
        }


        return true;
    }

    /**
     * Resets the game
     */
    public void newGame(){
      for (Tableau tab : tableaus)
      {
          tab.clear();
      }
      for (FreeCell free : freeCells)
      {
          free.clear();
      }
      for (HomeCell home : homeCells)
      {
          home.clear();
      }
        this.deal();
    }

    /**
     * Gives a string representation of the game
     * @return String representation of the game
     */
    public String toString()
    {
        String str;
        str = "Tableaus" + "\n" +
        "\n" + "Tableau 1: " + tableaus.get(0).toString() +
        "\n" + "Tableau 2: " + tableaus.get(1).toString() +
        "\n" + "Tableau 3: " + tableaus.get(2).toString() +
        "\n" + "Tableau 4: " + tableaus.get(3).toString() +
        "\n" + "Tableau 5: " + tableaus.get(4).toString() +
        "\n" + "Tableau 6: " + tableaus.get(5).toString() +
        "\n" + "Tableau 7: " + tableaus.get(6).toString() +
        "\n" + "Tableau 8: " + tableaus.get(7).toString() +
        "\n" + "\n" + "Free Cells" + "\n" +
        "\n" + "Free Cell 1: " + freeCells.get(0).toString() +
        "\n" + "Free Cell 2: " + freeCells.get(1).toString() +
        "\n" + "Free Cell 3: " + freeCells.get(2).toString() +
        "\n" + "Free Cell 4: " + freeCells.get(3).toString() +
        "\n" + "\n" + "Home Cells" + "\n" +
        "\n" + "Home Cell 1: " + homeCells.get(0).toString() +
        "\n" + "Home Cell 2: " + homeCells.get(1).toString() +
        "\n" + "Home Cell 3: " + homeCells.get(2).toString() +
        "\n" + "Home Cell 4: " + homeCells.get(3).toString() + "\n";

        return str;
    }
}
