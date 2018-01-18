class EvaluateConfig:
    def __init__(self):
        self.vram_frac = 1.0
        self.game_num = 2
        self.replace_rate = 0.55
        self.play_config = PlayConfig()
        self.play_config.simulation_num_per_move = 100 # before 200
        self.play_config.thinking_loop = 1
        self.play_config.c_puct = 1 # lower  = prefer mean action value
        self.play_config.tau_decay_rate = 0.6 # I need a better distribution...
        self.play_config.noise_eps = 0
        self.evaluate_latest_first = True
        self.max_game_length = 50  # before 1000


class PlayDataConfig:
    def __init__(self):
        self.min_elo_policy = 500 # 0 weight
        self.max_elo_policy = 1800 # 1 weight
        self.sl_nb_game_in_file = 250 # before 250
        self.nb_game_in_file = 10 #before 50
        self.max_file_num = 150


class PlayConfig:
    def __init__(self):
        self.max_processes = 2 #before 3
        self.search_threads = 4 #before 16
        self.vram_frac = 1.0
        self.simulation_num_per_move = 600 # before 1000
        self.thinking_loop = 1
        self.logging_thinking = False
        self.c_puct = 1.5
        self.noise_eps = 0.25
        self.dirichlet_alpha = 0.3
        self.tau_decay_rate = 0.99
        self.virtual_loss = 3
        self.resign_threshold = -0.8
        self.min_resign_turn = 5
        self.max_game_length = 10 # before 1000


class TrainerConfig:
    def __init__(self):
        self.min_games_to_begin_learn = 1000
        self.min_data_size_to_learn = 0
        self.cleaning_processes = 2 # before: 5 # RAM explosion...
        self.vram_frac = 1.0
        self.batch_size = 64 #before: 256 # tune this to your gpu memory
        self.epoch_to_checkpoint = 1
        self.dataset_size = 100000
        self.start_total_steps = 0
        self.save_model_steps = 25
        self.load_data_steps = 100
        self.loss_weights = [1.25, 1.0] # [policy, value] prevent value overfit in SL


class ModelConfig:
    cnn_filter_num = 256
    cnn_first_filter_size = 5
    cnn_filter_size = 3
    res_layer_num = 7
    l2_reg = 1e-4
    value_fc_size = 256
    distributed = False
    input_depth = 14
