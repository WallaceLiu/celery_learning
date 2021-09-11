import logging

from celery_wf_group_state.celery_app import app
from celery import group
from celery.result import allow_join_result
from time import sleep

# on_message回调值传递组任务内的任务进度, 更新组任务的进度需要获取group task对象
task_obj = None
# on_message回调每次只会返回一个子任务的任务进度, 做个全局进度保存
task_status = dict(
    task_A=dict(status="PROGRESS", progress=0, msg=""),
    task_B=dict(status="PROGRESS", progress=0, msg=""),
    task_C=dict(status="PROGRESS", progress=0, msg=""),
    task_D=dict(status="PROGRESS", progress=0, msg="")
)


def progress_update(meta_data):
    """
    更新进度的回调函数
    :param meta_data: 回调会自动获取任务反馈的进度meta_data
    :return: None
    """
    global task_obj
    global task_status

    logging.info("meta,meta,meta: {}".format(meta_data))

    if meta_data['result'] is not None:
        task_status[meta_data["result"]["task_name"]]["status"] = meta_data.get("status")
        if task_status["task_A"]["status"] == "SUCCESS" and task_status["task_B"]["status"] == "SUCCESS":
            group_status = "SUCCESS"
        elif task_status["task_A"]["status"] == "FAILED" or task_status["task_B"]["status"] == "FAILED":
            group_status = "FAILED"
        else:
            group_status = "PROGRESS"

        if meta_data.get("status") == "PROGRESS":
            task_status[meta_data["result"]["task_name"]]["progress"] = meta_data["result"]["progress"]
        if task_obj:
            logging.info("progress update, task_status: {}".format(task_status))
            task_obj.update_state(state=group_status, meta_data=dict(**task_status))
        else:
            logging.error("can't get global task_obj!")


@app.task(bind=True)
def group_task(self):
    """
    - 将被拆分的组任务，拆成以下两个子任务：
      - task_A
      - task_B
    """
    # 更新全局变量task_obj为当前组任务
    global task_obj
    task_obj = self

    group_task_id = self.request.id
    # 创建组任务
    res = group(A.s(group_task_id),
                B.s(group_task_id),
                C.s(group_task_id),
                D.s(group_task_id))()
    with allow_join_result():
        result = res.get(on_message=progress_update, propagate=False)
    logging.info("group task finish.")


#
# TASK A B C D
#

@app.task(bind=True)
def A(self, arg1):
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_A",
                          progress=0,
                          status="progress"
                      ))
    n = 0.1
    for i in range(10):
        ratio = n * i
        self.update_state(state="PROGRESS",
                          meta=dict(
                              task_name="task_A",
                              progress=ratio,
                              status="progress"
                          ))
    # 任务完毕
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_A",
                          progress=1,
                          status="finish"
                      ))


@app.task(bind=True)
def B(self, arg1):
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_B",
                          progress=0,
                          status="progress"
                      ))
    n = 0.1
    for i in range(10):
        ratio = n * i
        self.update_state(state="PROGRESS",
                          meta=dict(
                              task_name="task_B",
                              progress=ratio,
                              status="progress"
                          ))
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_B",
                          progress=1,
                          status="finish"
                      ))


@app.task(bind=True)
def C(self, arg1):
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_C",
                          progress=0,
                          status="progress"
                      ))
    n = 0.1
    for i in range(10):
        ratio = n * i
        self.update_state(state="PROGRESS",
                          meta=dict(
                              task_name="task_C",
                              progress=ratio,
                              status="progress"
                          ))
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_C",
                          progress=1,
                          status="finish"
                      ))


@app.task(bind=True)
def D(self, arg1):
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_D",
                          progress=0,
                          status="progress"
                      ))
    n = 0.1
    for i in range(10):
        ratio = n * i
        self.update_state(state="PROGRESS",
                          meta=dict(
                              task_name="task_D",
                              progress=ratio,
                              status="progress"
                          ))
    self.update_state(state="PROGRESS",
                      meta=dict(
                          task_name="task_D",
                          progress=1,
                          status="finish"
                      ))
