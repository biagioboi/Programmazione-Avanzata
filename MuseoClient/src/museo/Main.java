/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import java.util.List;
import java.util.Scanner;
import javax.jms.ConnectionFactory;
import javax.jms.Destination;
import javax.jms.JMSContext;
import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;

/**
 *
 * @author corsopd
 */
public class Main {
    
    //dimenticato di mettere il throws NamingException
    public static void main(String args[]) throws NamingException {
        Context ctx = new InitialContext();
        MuseoEJBRemote ejb = (MuseoEJBRemote) ctx.lookup("java:global/"
                + "MuseoBean/MuseoEJB!museo.MuseoEJBRemote");
        System.out.println("Inserire regione per ricerca: ");
        String regione = (new Scanner(System.in)).next();
        List<Museo> musei = ejb.printByRegion(regione);
        for (Museo m : musei) System.out.println(m);
        
        //parte relativa ai messaggi
        ConnectionFactory connection = (ConnectionFactory) ctx.lookup("jms/"
                + "javaee7/ConnectionFactory");
        Destination topic = (Destination) ctx.lookup("jms/javaee7/Topic");
        MessageDTO mess = new MessageDTO(2L, 5000);
        try (JMSContext context = connection.createContext()) {
            context.createProducer().send(topic, mess);
        }
        
    }
    
}
