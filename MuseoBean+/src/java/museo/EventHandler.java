/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import javax.enterprise.event.Observes;

/**
 *
 * @author corsopd
 */
public class EventHandler {
    public void notifica(@Observes Museo m) {
        System.out.println("Il numero di visitatori e' cambiato.");
    }
    
}
