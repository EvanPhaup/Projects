/**
 * A <code>HomeCell</code> gives functionality to home cells to be used in the game
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: HomeCell.java
 * The Home Cells are the cells that contain cards of all the same suit in order
 * from largest to smallest.
 */

import java.util.*;

/**
 * A home cell to be used in the free cell game model
 */
public class HomeCell extends AbstractCell{

  static public int MAX_SIZE = 13;

  /**
   * Initializes a new home cell
   */
  public HomeCell(){
    super(MAX_SIZE);
  }

  /**
   * Tells if a card can be moved to the home cell
   * @return True if the card can be moved
   */
  public boolean canMoveFrom(Cell from){
    if(! super.canMoveFrom(from)){
      return false;
    }
    else if(this.isEmpty() == true && from.peekTop().getRank() == 1){
      return true;
    }
    else if(this.isEmpty() == false && this.peekTop().getRank() + 1 == from.peekTop().getRank() && this.peekTop().getSuit() == from.peekTop().getSuit()){
      return true;
    }
    return false;

  }

  /**
   * Gives the max size
   * @return int max size
   */
  public int maxSize(){
    return this.MAX_SIZE;
  }
}
