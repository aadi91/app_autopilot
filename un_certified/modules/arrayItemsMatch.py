import os
import os.path
from pathlib import Path
from tkinter import filedialog

arrayFromJira = [
    "MANAGE_CREATE_UNI_OFFNET_ASRI_OL_V5.json",
    "Create_NID_ASRI_V2.json",
    "CreateNID_NL.json",
    "CreateNID_AL.json",
    "CREATE_UNI_DESIGN_ASRI_TL_V2.json",
    "CreateOffnetService_ASRI_TL_V2.json",
    "HW_GenerateOffnetServiceAliasName_NL_V2.json",
    "GetOffnetServiceAliasName_AL.json",
    "CreateOffnetService_ASRI_NL_V2.json",
    "CreateOffnetService_ASRI_AL.json",
    "HW_UNI_Offnet_OrderDetails.json",
    "HW_Offnet_Access_Request_V3.json",
    "HW_GetVtaAndSpecForPOM.json",
    "Get_IcscCodeFromEsl_NL.json",
    "HW_GetIcscCodeFromVendor_AL.json",
    "HW_GetOrchestrationIdForPom_V1.json",
    "HW_POM_Request_Details.json",
    "HW_Create_Offnet_BP_Validate_OL.json",
    "MANAGE_AMEND_UNI_OFFNET_ASRI_OL.json",
    "HW_UNI_RetainOffnetService.json",
    "AmendOffnetService_ASRI_TL.json",
    "POM_Offnet_Amend_Access_Request_V0.json",
    "UNI_Offnet_Fulfillment_Cust_CLLI_Costing_NL.json",
    "UNI_Offnet_Fulfillment_Cust_CLLI_Costing_AL.json",
    "HW_Get_POM_supVersion.json",
    "HW_POM_replace_request.json",
    "MANAGE_AMEND_UNI_OFFNET_NoServiceImpact.json",
    "POM_ASR_Vendor_Response_Handler.json",
    "HW_POM_Async_Callback_Handler.json",
    "HW_Create_Offnet_SLA_Update_OL.json",
    "Process_POM_FOC.json",
    "Process_POM_DLR.json",
    "Process_POM_Completion.json",
    "HW_FD_SLA_Async_Flows.json",
    "HW_FD_SLA_Async_FlowsNewCPELogic_V1.json",
    "HW_Update_New_SLA.json",
    "SIMPLE_WAN_UNI_Offnet_NID.json",
    "NID_Pre_Install_Fulfillment_TL_V2.json",
    "HW_GenerateFulfillmentRequestNumber_V1.json",
    "Get_NN_Details_For_ACT.json",
    "Get_UNI_For_NN_Details_NL.json",
    "Get_Transport_Details_For_NN_NL.json",
    "Assign_IP_Incognito_NL_V2.json",
    "Assign_IP_Incognito_AL.json",
    "Get_IPAddress_Tid_NL.json",
    "Get_IPAddress_Tid_AL.json",
    "NID_Shipping_Address_GLM_NL.json",
    "NID_Shipping_Details_GLM_AL.json",
    "Get_ConfigText_For_StageCoach_NL.json",
    "Get_ConfigText_For_StageCoach_AL.json",
    "HW_NID_shipment_Stagecoach_NL_V2.json",
    "HW_NID_shipment_Stagecoach_AL_V2.json",
    "NID_stageCoach_AsyncHandler.json",
    "HW_ShipmentTracker_V1.json",
    "HW_GetOffnetServiceAliasName.json",
    "Discover_Device_NEO_NL.json",
    "Discover_Device_NEO_AL_V2.json",
    "NID_Post_Install_Fulfillment_TL_V2.json",
    "BUILD_PORT_ACT_TL.json",
    "Validate_Device_NEO_NL.json",
    "Validate_Device_NEO_AL.json",
    "Validation_Results_NEO_NL.json",
    "Validation_Results_NEO_AL.json",
    "HW_UNIOffnetUpdate_TL.json",
    "HW_Offnet_UNI_IPAssignmentDetails_Fetch.json",
    "EMP_Event_OffnetUNIComplete_TL.json",
    "NAAS_UNI_Offnet_Cancel.json",
    "HW_UNI_OFFNET_CANCEL_CheckFlag.json",
    "UNI_Offnet_Cancel_AllActiveJobs.json",
    "HW_Get_CPE_NID_details.json",
    "FD_CANCEL_PENDING_TASKS_UNI_OFFNET.json",
    "HW_Cancel_CCD_Fulfilment_Tasks.json",
    "HW_Get_details_offnet_cancel_old_orders.json",
    "Delete_Order_SC_TL.json",
    "Delete_Order_SC_NL.json",
    "Delete_Order_SC_AL.json",
    "CANCEL_BUILD_PORT_ACT_TL.json",
    "Cancel_Buildresource_ACT_TL.json",
    "Un_Assign_IP_Incognito_TL.json",
    "Rollback_Offnet_ASRI_TL.json",
    "Rollback_UNI_ASRI_TL.json",
    "Rollback_NID_ASRI_TL",
]


# srcDirPath = filedialog.askdirectory()
def fn():  # 1.Get file names from directory
    file_list = os.listdir(
        r"/Users/shivaadityagoparaju/app/lib/github/AUTOPILOT-app-offnet/resources/itential/workflows/"
    )
    print(file_list)
    file_list = [9, 8, 7, 6, 5]
    matches1 = [i for i, j in zip(arrayFromJira, file_list) if i != j]
    print("Not Matched>>>>>>>>>>>>>>>>>>>>>>>>>>", matches1)


fn()
