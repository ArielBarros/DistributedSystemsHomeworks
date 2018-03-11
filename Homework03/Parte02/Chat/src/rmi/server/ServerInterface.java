package rmi.server;
import java.net.MalformedURLException;
import java.rmi.NotBoundException;
import java.rmi.Remote;
import java.rmi.RemoteException;


public interface ServerInterface extends Remote{
	void solicitarParticipacao(String cliente) throws RemoteException, MalformedURLException, NotBoundException;
	void solicitarSaida(String name) throws RemoteException;
	void enviarMensagem(String name, String message) throws RemoteException;
	void logServer(String name, String status) throws RemoteException;
}
