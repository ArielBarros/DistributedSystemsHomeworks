package rmi.cliente;

import java.rmi.Remote;
import java.rmi.RemoteException;

import rmi.server.ServerInterface;

public interface ClienteInterface extends Remote{
	
	String name = null;
	ServerInterface server = null;
	
	String getName() throws RemoteException;
	void recuperarMensagem(String mensagem) throws RemoteException;
}
