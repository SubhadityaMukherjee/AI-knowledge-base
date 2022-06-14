---
title: Basic RNN Architectures
tags: architecture einsum 
---

# Basic RNN Architectures
![[Pasted image 20220307171009.png]]

- [[Stacking RNN]]
- [[Bi Directional RNN]]
- [[Seq2Seq]]
- [[Temporal Conv]]
- [[Gated Recurrent Unit (GRU)]]

```python
class RNNModelNew(nn.Module):
    """Container module with an encoder, a recurrent module, and a decoder."""
    def __init__(self, ntoken, ninp, nhid, nlayers, dropout=0.5):
        super(RNNModel, self).__init__()
        self.drop = nn.Dropout(p=dropout)
        self.encoder = nn.Embedding(ntoken, ninp)
        self.rnn = nn.LSTM(ninp, nhid, nlayers, dropout=dropout)
        self.decoder = nn.Linear(nhid, ntoken)

    def forward(self, input, hidden):
        t, b = input.shape
        emb = self.drop(self.encoder(input))
        output, hidden = self.rnn(emb, hidden)
        output = rearrange(self.drop(output), 't b nhid -> (t b) nhid')
        decoded = rearrange(self.decoder(output), '(t b) token -> t b token', t=t, b=b)
        return decoded, hidden
```

```python
class RNNNew(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim, n_layers, bidirectional, dropout):
        super().__init__()
        
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.LSTM(embedding_dim, hidden_dim, num_layers=n_layers, 
                           bidirectional=bidirectional, dropout=dropout)
        self.dropout = nn.Dropout(dropout)
        self.directions = 2 if bidirectional else 1
        self.fc = nn.Linear(hidden_dim * self.directions, output_dim)
        
    def forward(self, x):
        #x = [sent len, batch size]        
        embedded = self.dropout(self.embedding(x))
        
        #embedded = [sent len, batch size, emb dim]
        output, (hidden, cell) = self.rnn(embedded)
        
        hidden = rearrange(hidden, '(layer dir) b c -> layer b (dir c)', 
                           dir=self.directions)
        # take the final layer's hidden
        return self.fc(self.dropout(hidden[-1]))
```




