// CalculDlg.cpp : implementation file
//

#include "stdafx.h"
#include "Calcul.h"
#include "CalculDlg.h"
#include "math.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };

	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CCalculDlg dialog

CCalculDlg::CCalculDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CCalculDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CCalculDlg)
	m_Result = _T("");
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}


void CCalculDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CCalculDlg)
	DDX_Text(pDX, IDC_EDIT1, m_Result);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CCalculDlg, CDialog)
	//{{AFX_MSG_MAP(CCalculDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, OnButton1)
	ON_BN_CLICKED(IDC_BUTTON2, OnButton2)
	ON_BN_CLICKED(IDC_BUTTON3, OnButton3)
	ON_BN_CLICKED(IDC_BUTTON4, OnButton4)
	ON_BN_CLICKED(IDC_BUTTON5, OnButton5)
	ON_BN_CLICKED(IDC_BUTTON6, OnButton6)
	ON_BN_CLICKED(IDC_BUTTON7, OnButton7)
	ON_BN_CLICKED(IDC_BUTTON8, OnButton8)
	ON_BN_CLICKED(IDC_BUTTON9, OnButton9)
	ON_BN_CLICKED(IDC_BUTTON10, OnButton10)
	ON_BN_CLICKED(IDC_BUTTON11, OnButton11)
	ON_BN_CLICKED(IDC_BUTTON12, OnButton12)
	ON_BN_CLICKED(IDC_BUTTON13, OnButton13)
	ON_BN_CLICKED(IDC_BUTTON14, OnButton14)
	ON_BN_CLICKED(IDC_BUTTON15, OnButton15)
	ON_BN_CLICKED(IDC_BUTTON16, OnButton16)
	ON_BN_CLICKED(IDC_BUTTON17, OnButton17)
	ON_BN_CLICKED(IDC_BUTTON18, OnButton18)
	ON_BN_CLICKED(IDC_BUTTON19, OnButton19)
	ON_BN_CLICKED(IDC_BUTTON20, OnButton20)
	ON_BN_CLICKED(IDC_BUTTON21, OnButton21)
	ON_BN_CLICKED(IDC_BUTTON27, OnButton27)
	ON_BN_CLICKED(IDC_BUTTON26, OnButton26)
	ON_BN_CLICKED(IDC_BUTTON25, OnButton25)
	ON_BN_CLICKED(IDC_BUTTON24, OnButton24)
	ON_BN_CLICKED(IDC_BUTTON23, OnButton23)
	ON_BN_CLICKED(IDC_BUTTON22, OnButton22)
	ON_COMMAND(ID_APP_ABOUT, OnAppAbout)
	ON_COMMAND(ID_EDIT_COPY, OnEditCopy)
	ON_COMMAND(ID_EDIT_PASTE, OnEditPaste)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CCalculDlg message handlers

BOOL CCalculDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	e=0;
	// TODO: Add extra initialization here
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CCalculDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CCalculDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}
void CCalculDlg::GetNum(CString num)
{
/*	if(m_N0 == "")   //m_N0��Ϊ��˵��
	{
		if(m_N2 == 0 )   //m_N2��Ϊ�㣬����ʾ���ǽ�������������¿�ʼһ�����֣�������ֱ�Ӽӵ����棬
		{
			UpdateData(TRUE);   //��һ�ΰ����ֻ�������
			m_Result += num ;
			UpdateData(FALSE); //�ѱ���m_Result �����༭��
		}
		else
		{
			m_Result =  num;   //����������ٴΰ�����������
			UpdateData(FALSE); //�ѱ���m_Result �����༭��
			m_N2 = 0;
		}
	}
	else
	{
		m_Result +=  num;   //��������ż�������
		UpdateData(FALSE); //�ѱ���m_Result �����༭��
	}
*/

	if(m_N0 == "")
	{
		if(m_N2 == 0)
		{
			UpdateData(TRUE);   //��һ�ΰ����ֻ�������
			{
			if( e == -1 )
			{
				m_Result = m_Result + "." + num;
				e = 1;
			}
			else
				m_Result += num ;
			}
			UpdateData(FALSE); //�ѱ���m_Result �����༭��
		}
		else
		{
			if(e == -1)
			{
				m_Result = "0." + num;
				e = 1;
			}
			else
				m_Result =  num;   //����������ٴΰ�����������
			UpdateData(FALSE); //�ѱ���m_Result �����༭��
			m_N2 = 0;
		}
	}
	else
	{
		if( e == -1 )
		{
			e = 1;
			m_Result = m_Result + "." + num;
		}
		else
			m_Result +=  num;   //��������ż�������
		UpdateData(FALSE); //�ѱ���m_Result �����༭��
	}
	

	
	/*�������ǿؼ�����Ϊdouble�Ͱ汾2
 	//UpdateData(TRUE);
	e = 0;
	m_N0.Format("%g",num);
	for(int i=0; i <m_N0.GetLength();i++)
	{
		if(m_N0.GetAt(i) == '.')
			e = -2 * (m_N0.GetLength() - i-1);
		else
			e++;
	}
*/
/***********
/**���ǿؼ�����Ϊdouble�Ͱ汾1  ת�����ж����С��β��Ϊ������  ����707.70070000
	
	e = 100;
	m_N0.Format("%f",num);
	for(int i = m_N0.GetLength();i > 0;i--)
	{
		//if((m_N0.GetAt(i) == '0')&& (e == 100) )   �﷨û������ᱨ��
		//{} else
		 if(m_N0.GetAt(i)=='.')
		{
			if(e == 100)
				e = 0;
			else
				e = 100-e;
		}
		else
		{
			e++;
		}
	}

	//return e;*/
}

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CCalculDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}



void CCalculDlg::OnButton1() 
{
	// TODO: Add your control notification handler code here
	 //�ѱ༭����ʾ���ַ���������Ӧ�ı���m_Result
	if(m_Result!="0" && m_Result.GetLength()>1)//��m_Result ������"0"��m_Result ���ȴ���1 ʱ
	{
		m_Result=m_Result.Left(m_Result.GetLength()-1);//ʹm_Result ���ȼ���1��ȥ�����ұߵ��ַ�
		UpdateData(FALSE);//���ַ�������m_strResult �����༭��
	}
}

void CCalculDlg::OnButton2() 
{
	// TODO: Add your control notification handler code here
	m_Result = "";  //�����ʾ
	e = 0;		//���С�����ע
	UpdateData(FALSE);  //�ϴ���ʾ
}

void CCalculDlg::OnButton3() 
{
	// TODO: Add your control notification handler code here
	m_Result = "";   //�����ʾ
	m_N0 = "";   //�������
	m_N1 = 0;
	m_N2 = 0;
	e = 0; 
	UpdateData(FALSE);
}

void CCalculDlg::OnButton4() 
{
	// TODO: Add your control notification handler code here
	m_M = 0;   //���M��־
	CWnd* pWnd = GetDlgItem(IDC_EDIT2);
	pWnd->SetWindowText(_T(""));   //���M��ʾ
	m_Result = "";   //�����ʾ
	m_N2 = 1; //��״̬��ɰ���Ⱥż����״̬�� �������ּ��ж��������¸�����ʾ
	e = 0; 
}

void CCalculDlg::OnButton5() 
{
	// TODO: Add your control notification handler code here
	GetNum("7");

/*//���ǿռ����Ϊdouble�͵İ汾
  UpdateData(TRUE);//�ѱ༭����ʾ�����ִ�����Ӧ�ı���m_Result
	Gete(m_Result);
	if(e< 0)
	{	e--;
		//
		m_Result = m_Result + 7*(pow(10,e));
	}
	else
		m_Result = m_Result * 10 + 7;
	UpdateData(FALSE); //�ѱ���m_Result �����༭��
	
	*/
}

void CCalculDlg::OnButton6() 
{
	// TODO: Add your control notification handler code here
	GetNum("8");
}

void CCalculDlg::OnButton7() 
{
	// TODO: Add your control notification handler code here
	GetNum("9");
}

void CCalculDlg::OnButton8() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")   
	{
		m_N1 = atof(m_Result.GetBuffer(16));
		
	}
	else 
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		if(m_N0 == "+")
			m_N1 += m_N2;
		else if(m_N0 == "-")
			m_N1 -= m_N2;
		else if(m_N0 == "*")
			m_N1 *= m_N2;
		else if(m_N0 == "/")
		{
			if(m_N2 == 0)
			{
				MessageBox("��������Ϊ�㣡",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //�ѱ���m_Result �����༭��	
	}
	m_N0 = "/";
	m_Result = "";
	e=0;
}

void CCalculDlg::OnButton9() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	m_N2 = atof(m_Result.GetBuffer(16));
	m_N2 = sqrt(m_N2);
	m_Result.Format("%g",m_N2);
	UpdateData(FALSE);
	e=0;
}

void CCalculDlg::OnButton10() 
{
	// TODO: Add your control notification handler code here
	m_Result.Format("%g",m_M);
	e = 0;
	UpdateData(FALSE);
	m_Result = "";   //�����ʾ
	m_N2 = m_M; //��״̬��ɰ���Ⱥż����״̬�� �������ּ��ж��������¸�����ʾ
}

void CCalculDlg::OnButton11() 
{
	// TODO: Add your control notification handler code here
	GetNum("4");
}

void CCalculDlg::OnButton12() 
{
	// TODO: Add your control notification handler code here
	GetNum("5");
}

void CCalculDlg::OnButton13() 
{
	// TODO: Add your control notification handler code here
	GetNum("6");
}

void CCalculDlg::OnButton14() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")
	{
		m_N1 = atof(m_Result.GetBuffer(16));
		
	}
	else 
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		if(m_N0 == "+")
			m_N1 += m_N2;
		else if(m_N0 == "-")
			m_N1 -= m_N2;
		else if(m_N0 == "*")
			m_N1 *= m_N2;
		else if(m_N0 == "/")
		{
			if(m_N2 == 0)
			{
				MessageBox("��������Ϊ�㣡",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //�ѱ���m_Result �����༭��	
	}
	m_N0 = "*";
	m_Result = "";
	e=0;
}

void CCalculDlg::OnButton15() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")
	{
		m_N1 = atof(m_Result.GetBuffer(16));
		m_N1 = m_N1 * 0.01;
		m_Result.Format("%g",m_N1);
	}
	else
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		m_N2 = m_N1 * m_N2 * 0.01;
		m_Result.Format("%g",m_N2);
	}
	UpdateData(FALSE);
	e=0;
}

void CCalculDlg::OnButton16() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	m_M = atof(m_Result.GetBuffer(16));
	CWnd* pWnd = GetDlgItem(IDC_EDIT2);
	pWnd->SetWindowText(_T("M"));
	m_N2 = m_M;  //��״̬��ɰ���Ⱥż����״̬�� �������ּ��ж��������¸�����ʾ
	m_Result = "";   //�����ʾ
}

void CCalculDlg::OnButton17() 
{
	// TODO: Add your control notification handler code here
	GetNum("1");
}

void CCalculDlg::OnButton18() 
{
	// TODO: Add your control notification handler code here
	GetNum("2");
}

void CCalculDlg::OnButton19() 
{
	// TODO: Add your control notification handler code here
	GetNum("3");
}

void CCalculDlg::OnButton20() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")
	{
		m_N1 = atof(m_Result.GetBuffer(16));
		
	}
	else 
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		if(m_N0 == "+")
			m_N1 += m_N2;
		else if(m_N0 == "-")
			m_N1 -= m_N2;
		else if(m_N0 == "*")
			m_N1 *= m_N2;
		else if(m_N0 == "/")
		{
			if(m_N2 == 0)
			{
				MessageBox("��������Ϊ�㣡",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //�ѱ���m_Result �����༭��	
	}
	m_N0 = "-";
	m_Result = "";
	e=0;
}

void CCalculDlg::OnButton21() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")
	{
		m_N1 = 1 / m_N1;
		m_Result.Format("%g",m_N1);
	}
	else
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		m_N2 = 1 / m_N2;
		m_Result.Format("%g",m_N2);
	}
	UpdateData(FALSE);
	e=0;
}

void CCalculDlg::OnButton27() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	m_N2 = atof(m_Result.GetBuffer(16));
	if(m_N0 == "+")
		m_N1 += m_N2;
	else if(m_N0 == "-")
		m_N1 -= m_N2;
	else if(m_N0 == "*")
		m_N1 *= m_N2;
	else if(m_N0 == "/")
	{
		if(m_N2 == 0)
		{
			MessageBox("��������Ϊ�㣡",ERROR,MB_OK|MB_ICONWARNING);
		}
		else
			m_N1 /= m_N2;
	}
	m_Result.Format("%g",m_N1);
	//m_N2 = 0;
	UpdateData(FALSE); //�ѱ���m_Result �����༭��
	m_N0 = "";
	m_Result = "";
	e=0;
}

void CCalculDlg::OnButton26() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if(m_N0 == "")
	{
		m_N1 = atof(m_Result.GetBuffer(16));
		
	}
	else 
	{
		m_N2 = atof(m_Result.GetBuffer(16));
		if(m_N0 == "+")
			m_N1 += m_N2;
		else if(m_N0 == "-")
			m_N1 -= m_N2;
		else if(m_N0 == "*")
			m_N1 *= m_N2;
		else if(m_N0 == "/")
		{
			if(m_N2 == 0)
			{
				MessageBox("��������Ϊ�㣡",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //�ѱ���m_Result �����༭��	
	}
	m_N0 = "+";
	m_Result = "";
	e=0;
}

void CCalculDlg::OnButton25() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if (m_Result != "")
	{
		if(e == 0)  //�ж��Ƿ��Ѿ���С��
		{
			e = -1;  //С�����жϱ�־
		}
	}
}

void CCalculDlg::OnButton24() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	if (m_Result != "")
	{
		if(atof(m_Result.GetBuffer(16)) >0)
			m_Result = "-" + m_Result;
		else if(atof(m_Result.GetBuffer(16)) < 0)
			m_Result = m_Result.Right(m_Result.GetLength() - 1);
	}
	UpdateData(FALSE);		
}

void CCalculDlg::OnButton23() 
{
	// TODO: Add your control notification handler code here
	GetNum("0");
}

void CCalculDlg::OnButton22() 
{
	// TODO: Add your control notification handler code here
	UpdateData(TRUE);
	m_M += atof(m_Result.GetBuffer(16));
	CWnd* pWnd = GetDlgItem(IDC_EDIT2);
	pWnd->SetWindowText(_T("M"));
	m_N2 = 1;  //��״̬��ɰ���Ⱥż����״̬�� �������ּ��ж��������¸�����ʾ
	e=0;
}

void CCalculDlg::OnAppAbout() 
{
	// TODO: Add your command handler code here
	ShellExecute(NULL,_T("OPEN"),_T("D:\\vc\\calculator1\\Calcul\\ReadMe.txt"),NULL,NULL,SW_SHOW);
}

void CCalculDlg::OnEditCopy() 
{
	// TODO: Add your command handler code here
	//int nStart, nEnd;
	UpdateData(TRUE);
	if (!OpenClipboard())  //����򲻿����а屨��
   {
      MessageBox(_T("Cannot open the Clipboard"),"����",MB_ICONERROR);
      return;
   }
   // Remove the current Clipboard contents  
   if(!EmptyClipboard())  //������а�Ϊ�ձ���
   {
      MessageBox(_T("Cannot empty the Clipboard"),"����",MB_ICONERROR);
      return;  
   }
	EmptyClipboard();//��ռ��а�,�õ�ǰ���ڽ���ӵ�м��а�
	HANDLE hClip;
	hClip=GlobalAlloc(GMEM_MOVEABLE,m_Result.GetLength()+1);//�����ڴ���󷵻ص�ַ(�ú�����ϵͳ��ȫ�ֶ��з����ڴ�)
	char *pBuf;
	pBuf=(char *)GlobalLock(hClip);//����ȫ���ڴ���ָ�����ڴ�飬������һ����ֵַ������ָ���ڴ�����ʼ��
	strcpy(pBuf,m_Result);//��Str�����е�����Copy���ڴ�ռ���
	GlobalUnlock(hClip);//����ȫ���ڴ��
    SetClipboardData(CF_TEXT,hClip);//���ü���������
    CloseClipboard();//�ر�
}

void CCalculDlg::OnEditPaste() 
{
	// TODO: Add your command handler code here
	if(IsClipboardFormatAvailable(CF_TEXT))//��ȡ��������ĸ�ʽ�Ƿ���Դ���  
	{  
	   if(OpenClipboard())  
	   {  
	    HANDLE hClip;  
	    char *pBuf;  
	    hClip=GetClipboardData(CF_TEXT); //������ָ����ʽ����������,������һ�������������  
	    pBuf=(char *)GlobalLock(hClip);//����ȫ���ڴ���ָ�����ڴ�� ������һ����ֵַ,����������ָ��ͷ��ַ  
	    GlobalUnlock(hClip);           //����  
	    SetDlgItemText(IDC_EDIT1,pBuf);  
	    CloseClipboard();  
	   }  
	}  
	e = 0;
	m_Result = "";
}
