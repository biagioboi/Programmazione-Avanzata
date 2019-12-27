/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.annotation.sql.DataSourceDefinition;
import javax.ejb.Singleton;
import javax.ejb.Startup;
import javax.inject.Inject;

/**
 *
 * @author corsopd
 */
@Singleton
@Startup
@DataSourceDefinition(
        className = "org.apache.derby.jdbc.ClientDriver",
        databaseName = "EsameDB",
        user = "APP",
        password = "APP",
        name = "java:global/jdbc/EsameDS",
        properties = "connectionAttributes=;create=true"
)
public class DatabasePopulator {
    @Inject
    MuseoEJB ejb;
    private Museo paestum, vaticani, uffizi;
    
    @PostConstruct
    public void inizializza() {
        paestum = new Museo("Museo di Paestum", "Gabriel Zuchtriegel", 430000, 
                            "Capaccio", "Salerno", "Campania");
        vaticani = new Museo("Musei Vaticani", "Barbara Jatta", 5978804,
                             "Roma", "Roma", "Lazio");
        uffizi = new Museo("Galleria degli Uffizi", "Eike Dieter Schmidt",
                           1935901, "Firenze", "Firenze", "Toscana");
        ejb.createMuseo(paestum);
        ejb.createMuseo(vaticani);
        ejb.createMuseo(uffizi);
    }
    
    @PreDestroy
    public void distruggi() {
        ejb.deleteMuseo(paestum);
        ejb.deleteMuseo(vaticani);
        ejb.deleteMuseo(uffizi);
    }
}
