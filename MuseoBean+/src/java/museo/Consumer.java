/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import javax.ejb.ActivationConfigProperty;
import javax.ejb.MessageDriven;
import javax.enterprise.event.Event;
import javax.inject.Inject;
import javax.jms.JMSException;
import javax.jms.Message;
import javax.jms.MessageListener;

/**
 *
 * @author corsopd
 */
@MessageDriven(
        mappedName = "jms/javaee7/Topic",
        activationConfig = {
            @ActivationConfigProperty (
                    propertyName = "acknowledgeMode",
                    propertyValue = "Auto-acknowledge"
            )
        }
)
public class Consumer implements MessageListener{
    @Inject
    Event<Museo> event;
    @Inject
    MuseoEJB ejb;
    
    public void onMessage(Message msg) {
        try {
            // ho dimenticato di scrivere la classe del body e non ho
            // gestito l'eccezione
            MessageDTO mex = (MessageDTO) msg.getBody(MessageDTO.class);
            Museo m = ejb.retrieveById(mex.getIdMuseo());
            m.setVisitatori(mex.getNumVisitatori());
            ejb.updateMuseo(m);
            event.fire(m);
        } catch (JMSException ex) {
            System.out.println("Errore");
        }
        
    }
    
}
