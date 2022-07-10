/**
 * A <code>abstractCell</code> Abstract cell panel for specific cell panels to use
 * @author Bryce Burnette
 * @author Ana Estrada Hamm
 * @author Evan Phaup
 * file: AbstractCellPanel.java
 */

import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * Abstract cell panel class to be used in cell panel implementation
 * Implements CellPanel interface
 */
abstract public class AbstractCellPanel extends JPanel implements CellPanel{

    private Cell cell;

    /**
     * Initializes an abstract cell panel
     */
    public AbstractCellPanel()
    {

    }
    
    /**
     * initializes an abstract cell panel
     * @param c the cell inside of the panel
     */
    public AbstractCellPanel(Cell c)
    {
        cell = c;
    }

    /**
     * Sets up the panel for display.
     */
    public void paintComponent(Graphics g){
        setBackground(Color.black);
        int cardNumber = 0;
        Icon image;
        if (this.cell.isEmpty() == true)
        {
            image = Card.getBack();
    		g.setColor(Color.yellow);
    		int x = (getWidth() - image.getIconWidth()) / 2;
    		int y = (getHeight() - image.getIconHeight()) / 2;
            g.drawRect(x, y, image.getIconWidth(), image.getIconHeight());
        }
        else
        {
            for (Card card : this.cell.cards()){
                image = card.getImage();
                int x = (getWidth() - image.getIconWidth()) / 2;
                int y = (getHeight() - image.getIconHeight()) / 2;
                image.paintIcon(this, g, x, y - cardNumber);
                cardNumber++;
            }
        }
    }

    /**
     * Sets the cell that the panel will contain
     * @param cell to be contained
     */
    public void setCell(Cell c){
    	this.cell = c;
      repaint();
    }

    /**
     * @return the cell that the panel contains
     */
    public Cell getCell()
    {
        return this.cell;
    }
}