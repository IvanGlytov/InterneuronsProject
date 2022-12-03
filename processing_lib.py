

def get_ripples_episodes_indexes(lfp, fs):
    """
    :param lfp: сигнал lfp
    :param fs: частота дискретизации
    :return:  массив начал и концов риппл событий
    """

    pass

def get_theta_non_theta_epoches(theta_lfp, delta_lfp):
    """
    :param theta_lfp: отфильтрованный в тета-диапазоне LFP
    :param delta_lfp: отфильтрованный в дельа-диапазоне LFP
    :return: массив индексов начала и конца тета-эпох, другой массив для нетета-эпох
    """
    pass

def get_circular_mean_R(filtered_lfp, fs, spike_train):
    """
    :param filtered_lfp: отфильтрованный в нужном диапазоне LFP
    :param fs: частота дискретизации
    :param spike_train: времена импульсов
    :return: циркулярное среднее и R
    """

def get_mean_spike_rate_by_epoches(spike_train, epoches):
    """
    :param epoches: массив начал и концов эпох
    :param spike_train: времена импульсов
    :return: циркулярное среднее и R
    """
    pass


class InterneuronClassifier:

    def __int__(self, path2data):
        """
        :param path2data: Путь к файлу с данными, покоторым будем классифицировать
        :return:
        """

    def transpose(self, X):
        """
        :param X: вектор - описание потока импульсов
        :return: class name
        """

        
class Filtrator():
    def __init__(self, lowcut, highcut, fs, order):
        self.fs = fs
        self.nyq = self.fs * 0.5
        self.lowcut = lowcut / self.nyq
        self.highcut = highcut / self.nyq
        self.order = order
        self.b, self.a = signal.butter(N=self.order, Wn=[self.lowcut, self.highcut], btype='bandpass')
    
    def butter_bandpass_filter(self, lfp):
        filtered = signal.filtfilt(self.b, self.a, lfp)
        return filtered 
        


