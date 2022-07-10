/**
 * A <code>FreeCell</code> gives functionality to free cell to be used in the game
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: FreeCell.java
 */

 import java.util.*;

 /**
  * free cells to be used in the free cell game model
  */
 public class FreeCell extends AbstractCell{
   static public int MAX_SIZE = 1;
  /**
   * Initializes a free cell
   */
  public FreeCell(){
    super(MAX_SIZE);
  }

  /**
   * Checks to cee if a card can be moved to this cell
   * @return true if the card can be moved to this cell
   */
  public boolean canMoveFrom(Cell from){
    if(! super.canMoveFrom(from)){
      return false;
    }
    else if(this.isEmpty()){
      return true;
    }
    return false;
  }
 }
