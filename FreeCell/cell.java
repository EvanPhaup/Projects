/**
 * A <code>Cell</code> plays the game of war
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: Cell.java
 * project6
 * This is an interface for cells found in free-cell solitaire.
 */

import java.util.*;

/**
 * Interface to be used for different types of cells
 */
public interface Cell extends Iterable <Card>{

  /**
  * @return boolean
  * checks if the cell is empty. If the cell has no cards return true. If cell
  * has cards return false.
  */
  public boolean isEmpty();

  /**
   * Gives the size of the cell
   * @return int size of the cell
   */
  public int size();

  /**
   * Clears the cell
   */
  public void clear();

  //public boolean canMoveFrom();
  //public Card getTop(){}

  /**
   * Gives the max size of the cell
   * @return int max size of the cell
   */
  public int maxSize();

  /**
   * Gives the card at the top of cell
   * @return Card at top of cell
   */
  public Card peekTop();

  /**
   * Removes and returns card from top of cell
   * @return Card at top of cell
   */
  public Card getTop();
  public ArrayList<Card> cards();
  public void addFrom(Cell from);
  public boolean canMoveFrom(Cell from);
  public void add(Card c);
  //public boolean isGroupValid(int startingIndex);
  //public ArrayList<Card> getGroupCards(int startingIndex);
  //public boolean addGroupCards(ArrayList<Card> group);
}
