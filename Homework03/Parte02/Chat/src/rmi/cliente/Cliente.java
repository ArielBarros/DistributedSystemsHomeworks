package rmi.cliente;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

import rmi.server.ServerInterface;

public class Cliente extends UnicastRemoteObject implements ClienteInterface, Runnable{

	private static final long serialVersionUID = 1L;

	private String name;
	private ServerInterface server;
	private Scanner scanner;

	protected Cliente(String name, ServerInterface server) throws RemoteException, MalformedURLException, NotBoundException {
		this.name = name;
		this.server = server;
		Naming.rebind(name, this);
		server.solicitarParticipacao(name);
	}

	@Override
	public void recuperarMensagem(String mensagem) throws RemoteException {
		System.out.println(mensagem);
	}

	@Override
	// Função que roda o cliente após ele ter se conectado com o servidor
	// e lê as entradas dele.
	public void run() {
		scanner = new Scanner(System.in);
		String mensagem = null;
		System.out.println("Digite SAIR para sair do chat e depois Ctrl+C para sair do programa");
		while(true) {
			try {
				// Lê as entradas
				mensagem = scanner.nextLine();
			} catch (Exception e) {
				System.out.println("Ate a proxima !!");
				System.exit(0);
			}
			try {
				// Envia entrada do cliente para o servidor
				server.enviarMensagem(this.name, mensagem);
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

	@Override
	public String getName() throws RemoteException{
		return this.name;
	}
}
