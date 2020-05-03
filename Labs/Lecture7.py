import matplotlib.pyplot as plt
import numpy as np
from hamming_weight import hamming_weight
from aes_scripts.aes_crypt_8bit import aes_crypt_8bit
from aes_scripts.aes_crypt_8bit_and_leak import aes_crypt_8bit_and_leak

#  Differential power analysis and correlation power analysis
DPA = 0
CPA = 1
dpa_or_cpa = CPA # DPA


# #
#  Make sure the matlab AES scripts are in the path

#  Load WS2, show a few traces
load ws2
disp(size(traces)) #  D = 200, T = 100000
#  shrink it a little so it runs faster
traces = traces(:,1:30000)
input_count = size(traces,1)
trace_length = size(traces,2)
# #
plot([traces(1,:);traces(2,:)]')
xlim([300 500])
# figure(gcf)
# #
#  We want to guess byte 1 in the key
key_byte_to_guess = 12;
classification_output = zeros(2^8, trace_length)
disp(size(classification_output))
# #
#  For each key gues
trace_classification = zeros(2^8, input_count)

for key_guess = 0:1:2^8-1



%%
% Plot the trace classification matrix
imagesc(trace_classification)
xlabel('Trace index')
ylabel(['Key guess for byte ' num2str(key_byte_to_guess)])
figure(gcf)
%%
% CPA only: show the actual power consumption at correct time, compared to
% power model
plot([traces(:,correct_time)./5, trace_classification(correct_key,:)'])
xlabel('Trace index')
ylabel({'Power consumption at correct time (blye)','Power model for correct key (red)'})
%%
% Find out the correct timne and correct key
[~, correct_time] = max(max(abs(classification_output)));
[~, correct_key] = max(abs(classification_output(:,correct_time))); % this is actually correct_key + 1
bar(abs(classification_output(:,correct_time)))
xlabel('Key guess')
%%
% plot the correct key at the correct time
plot(classification_output');xlim([correct_time-100 correct_time+100]);
hold on
plot(classification_output(correct_key,:),':','LineWidth',5);
hold off
figure(gcf)