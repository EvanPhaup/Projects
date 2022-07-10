/**
 * A <code>Tableau</code> The tableau used in the game of free cell
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: Tableau.java
 * has to be the opposite color to stack-- check to if the rank is one greater
 */

import java.util.*;

/**
 * Tableau cell to be used in the free cell game model
 */
public class Tableau extends AbstractCell{

  static public int MAX_SIZE = 26;

  /**
   * Initializes a tableau
   */
  public Tableau(){
    super(MAX_SIZE);
  }

  /**
   * Tells if a card can be moved from a cell to the tableau
   * @return true if the card can be moved
   */
  public boolean canMoveFrom(Cell from){
    if(!super.canMoveFrom(from)){
            return false;
    }
    else if(this.isEmpty() == true){
      return true;
    }
    else if(this.peekTop().getRank() - 1 == from.peekTop().getRank() && ! (this.peekTop().getColor() == from.peekTop().getColor())){
      return true;
    }
    return false;
  }

  /**
   * Checks to see if a group of cards is in order
   * @param i the starting index, checks to see if all cards after this are in order
   * @return true if the cards are in order
   */
  public boolean inOrder(int i)
  {
    while(i < this.cards.size() - 1) 
      {
        if ((! (this.cards().get(i).getRank() == this.cards().get(i + 1).getRank() + 1)) ||
        (this.cards().get(i).getColor() == this.cards().get(i + 1).getColor()) || (i == this.cards().size() - 1))
        {
          return false;
        }
        else
        {
          i++;
        }
      }
    return true;  
  }

  /**
   * Checks to see if a group of cards is valid to be moved
   * @param startingIndex where the group to be moved starts in the list of cards
   * @return true if the cards can be moved
   */
  public boolean isGroupValid(int startingIndex, Cell cellTo){
    int i = startingIndex;

    if (this.isEmpty()){
      return false;
    }

    if (cellTo.isEmpty())
    {
      return this.inOrder(i);
    }

    while (i < this.cards().size() - 1){
      if ((! (this.cards().get(i).getRank() == this.cards().get(i + 1).getRank() + 1)) ||
      (this.cards().get(i).getColor() == this.cards().get(i + 1).getColor()) || (startingIndex == this.cards().size() - 1)){
        return false;
      }
      i++;
    }
    while(i >= startingIndex){
      if(this.cards.get(i).getRank() == cellTo.peekTop().getRank() - 1 && this.cards.get(i).getColor() != cellTo.peekTop().getColor()){
        return true;
      }
      else{
        i -= 1;
      }
    }
    return false;
  }

  /**
   * Gets the index where the group of cards starts in the tableau based on 
   * where the cards are going and if they are in order
   * @param cellTo the cell that the cards are going to
   * @return int - the index that the group starts at
   */
  public int getStartingIndex(Cell cellTo){
    int i = 0;
    
    while (i < this.cards.size())
    {
      if ((this.cards.get(i).getRank() == (cellTo.peekTop().getRank() - 1)) && (this.cards.get(i).getColor() != cellTo.peekTop().getColor()) && this.inOrder(i))
      {
        System.out.println("Index to use: " + i);
        return i;
      }
      i++;
    }
    return this.cards.size();
  }

  /**
   * Collects the group of cards to be moved
   * @param startingIndex starting index of card to be collected
   * @return the cards collected from the starting index to the top of the cell
   */
  public ArrayList<Card> getGroupCards(int startingIndex, Cell cellTo){
    ArrayList<Card> group = new ArrayList<Card>();
    int i;
    int size = this.cards.size();

    if (cellTo.isEmpty())
    {
      i = startingIndex;
      if (this.isGroupValid(i, cellTo)){
        while (i < size){
          group.add(this.cards().remove(i));
          size = this.cards.size();
        }
      }
    }
    
    else
    {
      i = getStartingIndex(cellTo);
      if (this.isGroupValid(i, cellTo)){
        while (i < size){
          group.add(this.cards().remove(i));
          size = this.cards.size();
        }
      }
      else
      {
        return null;
      }
    }
    return group;
  }

  /**
   * Adds a valid group of cards to the cell
   * @param group array list of cards to be added
   */
  public boolean addGroupCards(ArrayList<Card> group)
  {
    if (group.isEmpty() == false && (this.cards().isEmpty() == true || (group.get(0).getRank() == peekTop().getRank() - 1
    && !(group.get(0).getColor() == peekTop().getColor()))))
    {
      for (Card item : group)
      {
        this.add(item);
      }
      return true;
    }
    return false;
  }
}
