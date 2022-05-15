# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook', by_epoch=True),
        # dict(type='TensorboardLoggerHook')
    dict(
            type="WandbLoggerHook",
            init_kwargs=dict(
                project='semantic_segmentation',
				entity='snow-man',
                name='hj_beit_l_full_2',
            ),
        ),
    ],
)


# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
cudnn_benchmark = True

# fp16 settings
optimizer_config = dict(type='Fp16OptimizerHook', loss_scale=512.)
# fp16 placeholder
fp16 = dict()