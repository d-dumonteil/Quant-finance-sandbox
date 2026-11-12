import numpy as np

def crr_params(S0, sigma, r, T, N):
    dt = T/N
    u = np.exp(sigma*np.sqrt(T/N))
    d = 1/u
    q = (np.exp(r*dt)-d)/(u-d)
    disc = np.exp(-r*dt)
    return dt,u,d,q,disc

def terminal_prices(S0, u, d, N):
    return 

def payoff_call(S, K):
    return 

def payoff_put(S, K):
    return 

def price_european(S0, K, sigma, r, T, N, payoff):
    return 

def price_american(S0, K, sigma, r, T, N, payoff):
    return 

def greeks(S0, K, sigma, r, T, N, payoff, pricer):
    return 

def convergence_study(S0, K, sigma, r, T, payoff):
    return 


def main():
    return 0

if __name__ == "__main__":
    main()