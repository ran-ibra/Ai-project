import matplotlib.pyplot as plt

def compare(minimax_execution_times,alpha_beta_execution_times,minimax_node_evaluations,alpha_beta_node_evaluations):
    plt.figure(figsize=(8, 6))
    plt.subplot(2, 1, 1)
    plt.plot(minimax_execution_times, label='Minimax')
    plt.plot(alpha_beta_execution_times, label='Alpha-Beta Pruning')
    plt.xlabel('Iteration')
    plt.ylabel('Execution Time')
    plt.title('Algorithm Execution Time')
    plt.legend()
    plt.subplot(2, 1, 2)
    plt.plot(minimax_node_evaluations, label='Minimax')
    plt.plot(alpha_beta_node_evaluations, label='Alpha-Beta Pruning')
    plt.xlabel('Iteration')
    plt.ylabel('Node Evaluations')
    plt.title('Node Evaluations')
    plt.legend()

    plt.tight_layout()
    plt.show()
