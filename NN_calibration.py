import torch
import torch.nn as nn
import torch.optim as optim

class TemperatureScaling(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.temperature = nn.Parameter(torch.ones(1) * 1.0)

    def forward(self, x):
        logits = self.model(x)
        return logits / self.temperature

    def set_temperature(self, valid_loader):
        self.eval()
        nll_criterion = nn.CrossEntropyLoss()
        optimizer = optim.LBFGS([self.temperature], lr=0.01, max_iter=50)

        logits_list = []
        labels_list = []
        with torch.no_grad():
            for inputs, labels in valid_loader:
                logits = self.model(inputs)
                logits_list.append(logits)
                labels_list.append(labels)
        logits = torch.cat(logits_list)
        labels = torch.cat(labels_list)

        def eval():
            optimizer.zero_grad()
            loss = nll_criterion(logits / self.temperature, labels)
            loss.backward()
            return loss

        optimizer.step(eval)
        print(f"Optimal temperature: {self.temperature.item()}")

# Example usage:
# calibrated_model = TemperatureScaling(pretrained_model)
# calibrated_model.set_temperature(validation_loader)

# To get calibrated probabilities on new data:
# logits = calibrated_model(new_inputs)
# probs = torch.softmax(logits, dim=1)
