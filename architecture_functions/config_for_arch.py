CONFIG_ARCH = {
    'logging' : {
        'path_to_log_file' : './logs/logger/',
        'path_to_tensorboard_logs' : './logs/architectures_training/fbnet_transformer_binary_tb8'
    },
    'dataloading' : {
        'batch_size' : 1000,
        'train_portion' : 0.8,
        'path_to_save_data' : './datasets'
    },
    'optimizer' : {
        'lr' : 0.1,
        'momentum' : 0.9,
        'weight_decay' : 4 * 1e-5
    },
    'train_settings' : {
        'print_freq' : 50, # show logging information
        'path_to_save_model' : './models/best_model.pth',
        'cnt_epochs' : 60, # 140
        # YOU COULD USE 'CosineAnnealingLR' or 'MultiStepLR' scheduler
        'scheduler' : 'MultiStepLR',
        ## CosineAnnealingLR settings
        'eta_min' : 0.001,
        ## MultiStepLR settings
        'milestones' : [90, 110], # [90, 180, 270], # decay 10x at 90, 180, and 270 epochs
        'lr_decay' : 0.1
    }
}