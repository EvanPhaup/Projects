/**
 * A <code>Cell</code> plays the game of war
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: CellPanel.java
 * This is an interface for cells found in free-cell solitaire.
 */

/**
 * Interface to be used for different types of cell pannels
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public interface CellPanel{

    public void paintComponent(Graphics g);
    public void setCell(Cell c);
    public Cell getCell();

}