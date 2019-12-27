/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package museo;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;

/**
 *
 * @author corsopd
 */
@Entity
@NamedQueries({
    @NamedQuery(name = Museo.retrieveById, query = "SELECT m FROM Museo m WHERE m.id = :id"),
    @NamedQuery(name = Museo.retrieveByRegione, query = "SELECT m FROM Museo m WHERE m.regione = :regione"),
    @NamedQuery(name = Museo.retrieveAll, query = "SELECT m FROM Museo m")
})
public class Museo implements Serializable{
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;
    private String nome;
    private String direttore;
    private int visitatori;
    private String citta;
    private String provincia;
    private String regione;
    
    //avevo dimenticato di definire le costanti per le query
    public static final String retrieveById = "Museo.retrieveById";
    public static final String retrieveByRegione = "Museo.retrieveByRegione";
    public static final String retrieveAll = "Museo.retrieveAll";

    public Museo() {
    }

    public Museo(String nome, String direttore, int visitatori, String citta, String provincia, String regione) {
        this.nome = nome;
        this.direttore = direttore;
        this.visitatori = visitatori;
        this.citta = citta;
        this.provincia = provincia;
        this.regione = regione;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDirettore() {
        return direttore;
    }

    public void setDirettore(String direttore) {
        this.direttore = direttore;
    }

    public int getVisitatori() {
        return visitatori;
    }

    public void setVisitatori(int visitatori) {
        this.visitatori = visitatori;
    }

    public String getCitta() {
        return citta;
    }

    public void setCitta(String citta) {
        this.citta = citta;
    }

    public String getProvincia() {
        return provincia;
    }

    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }

    public String getRegione() {
        return regione;
    }

    public void setRegione(String regione) {
        this.regione = regione;
    }
    
    
}
