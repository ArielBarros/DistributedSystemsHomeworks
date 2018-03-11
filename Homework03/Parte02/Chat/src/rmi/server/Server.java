package rmi.server;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import rmi.cliente.ClienteInterface;

public class Server extends UnicastRemoteObject implements ServerInterface {

	private static final long serialVersionUID = 1L;
	private ArrayList<ClienteInterface> listaClientes;

	protected Server() throws RemoteException {
		// Inicia uma lista vazia de clientes
		listaClientes = new ArrayList<ClienteInterface>();
	}

	@Override
	// Método que registra o cliente na lista de troca de mensagens
	public synchronized void solicitarParticipacao(String name) throws RemoteException, MalformedURLException, NotBoundException {
		String URIcliente = "rmi://localhost/"+ name;
		ClienteInterface cliente = (ClienteInterface) Naming.lookup(URIcliente);
		this.listaClientes.add(cliente);
		logServer(name, "CONECTADO");
		enviarMensagem("Cliente: "+ name, "[ENTROU NA CONVERSA]");
	}

	@Override
	// Método para tirar o registro de um cliente da lista de troca de mensagens
	public void solicitarSaida(String name) throws RemoteException {
		int i = 0;
		ClienteInterface cliente;
		/// Método para mostrar o status atual do servidor após a entrada
		// ou saída de um cliente da lista.
		while(i < listaClientes.size()) {
			cliente = listaClientes.get(i);
			if((cliente.getName()).equals(name)){
				listaClientes.remove(i);
				enviarMensagem("Cliente: "+ name, "[SAIU DA CONVERSA]");
				break;
			}
			i++;
		}
	}

	@Override
	// Método para mostrar o status atual do servidor após a entrada
	// ou saída de um cliente da lista.
	public void logServer(String name, String status) throws RemoteException{
		System.out.println("Cliente: "+name+" ["+status+"]");
		System.out.println("Numero de clientes conectados: " + listaClientes.size());
	}

	@Override
	// Envia a mensagem de um cliente para todos os outros conectados através de um RMI.
	public synchronized void enviarMensagem(String name, String mensagem) throws RemoteException {
		int i = 0;
		ClienteInterface cliente;

		if(mensagem.equals("SAIR")) {
			solicitarSaida(name);
			logServer(name, "DESCONECTADO");
		} else {
			while(i < listaClientes.size()) {
				cliente = listaClientes.get(i++);
				// Condicional para evitar que a mensagem seja enviada ao remetente
				if( ! (cliente.getName()).equals(name) ) {
					cliente.recuperarMensagem(name + ": "+mensagem);
				}
			}
		}
	}
}
