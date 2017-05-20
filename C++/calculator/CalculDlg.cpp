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
/*	if(m_N0 == "")   //m_N0不为空说明
	{
		if(m_N2 == 0 )   //m_N2不为零，则显示的是结果，按下需重新开始一个数字，而不是直接加到后面，
		{
			UpdateData(TRUE);   //第一次按数字会走这里
			m_Result += num ;
			UpdateData(FALSE); //把变量m_Result 传给编辑框
		}
		else
		{
			m_Result =  num;   //当计算完后，再次按数字走这里
			UpdateData(FALSE); //把变量m_Result 传给编辑框
			m_N2 = 0;
		}
	}
	else
	{
		m_Result +=  num;   //当按完符号键走这里
		UpdateData(FALSE); //把变量m_Result 传给编辑框
	}
*/

	if(m_N0 == "")
	{
		if(m_N2 == 0)
		{
			UpdateData(TRUE);   //第一次按数字会走这里
			{
			if( e == -1 )
			{
				m_Result = m_Result + "." + num;
				e = 1;
			}
			else
				m_Result += num ;
			}
			UpdateData(FALSE); //把变量m_Result 传给编辑框
		}
		else
		{
			if(e == -1)
			{
				m_Result = "0." + num;
				e = 1;
			}
			else
				m_Result =  num;   //当计算完后，再次按数字走这里
			UpdateData(FALSE); //把变量m_Result 传给编辑框
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
			m_Result +=  num;   //当按完符号键走这里
		UpdateData(FALSE); //把变量m_Result 传给编辑框
	}
	

	
	/*这是这是控件变量为double型版本2
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
/**这是控件变量为double型版本1  转换后有多余的小数尾数为零的情况  例如707.70070000
	
	e = 100;
	m_N0.Format("%f",num);
	for(int i = m_N0.GetLength();i > 0;i--)
	{
		//if((m_N0.GetAt(i) == '0')&& (e == 100) )   语法没错，程序会报错
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
	 //把编辑框显示的字符串传给相应的变量m_Result
	if(m_Result!="0" && m_Result.GetLength()>1)//当m_Result 不等于"0"且m_Result 长度大于1 时
	{
		m_Result=m_Result.Left(m_Result.GetLength()-1);//使m_Result 长度减少1，去掉最右边的字符
		UpdateData(FALSE);//把字符串变量m_strResult 传给编辑框
	}
}

void CCalculDlg::OnButton2() 
{
	// TODO: Add your control notification handler code here
	m_Result = "";  //清空显示
	e = 0;		//清除小数点标注
	UpdateData(FALSE);  //上传显示
}

void CCalculDlg::OnButton3() 
{
	// TODO: Add your control notification handler code here
	m_Result = "";   //清空显示
	m_N0 = "";   //清除数据
	m_N1 = 0;
	m_N2 = 0;
	e = 0; 
	UpdateData(FALSE);
}

void CCalculDlg::OnButton4() 
{
	// TODO: Add your control notification handler code here
	m_M = 0;   //清除M标志
	CWnd* pWnd = GetDlgItem(IDC_EDIT2);
	pWnd->SetWindowText(_T(""));   //清除M显示
	m_Result = "";   //清空显示
	m_N2 = 1; //把状态变成按完等号键后的状态， 好让数字键判断能走重新覆盖显示
	e = 0; 
}

void CCalculDlg::OnButton5() 
{
	// TODO: Add your control notification handler code here
	GetNum("7");

/*//这是空间变量为double型的版本
  UpdateData(TRUE);//把编辑框显示的数字传给相应的变量m_Result
	Gete(m_Result);
	if(e< 0)
	{	e--;
		//
		m_Result = m_Result + 7*(pow(10,e));
	}
	else
		m_Result = m_Result * 10 + 7;
	UpdateData(FALSE); //把变量m_Result 传给编辑框
	
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
				MessageBox("除数不能为零！",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //把变量m_Result 传给编辑框	
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
	m_Result = "";   //清空显示
	m_N2 = m_M; //把状态变成按完等号键后的状态， 好让数字键判断能走重新覆盖显示
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
				MessageBox("除数不能为零！",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //把变量m_Result 传给编辑框	
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
	m_N2 = m_M;  //把状态变成按完等号键后的状态， 好让数字键判断能走重新覆盖显示
	m_Result = "";   //清空显示
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
				MessageBox("除数不能为零！",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //把变量m_Result 传给编辑框	
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
			MessageBox("除数不能为零！",ERROR,MB_OK|MB_ICONWARNING);
		}
		else
			m_N1 /= m_N2;
	}
	m_Result.Format("%g",m_N1);
	//m_N2 = 0;
	UpdateData(FALSE); //把变量m_Result 传给编辑框
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
				MessageBox("除数不能为零！",ERROR,MB_OK|MB_ICONWARNING);
			}
			else
				m_N1 /= m_N2;
		}
		m_Result.Format("%g",m_N1);
		m_N2 = 0;
	    UpdateData(FALSE); //把变量m_Result 传给编辑框	
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
		if(e == 0)  //判断是否已经是小数
		{
			e = -1;  //小数点判断标志
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
	m_N2 = 1;  //把状态变成按完等号键后的状态， 好让数字键判断能走重新覆盖显示
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
	if (!OpenClipboard())  //如果打不开剪切板报错
   {
      MessageBox(_T("Cannot open the Clipboard"),"错误",MB_ICONERROR);
      return;
   }
   // Remove the current Clipboard contents  
   if(!EmptyClipboard())  //如果剪切板为空报错
   {
      MessageBox(_T("Cannot empty the Clipboard"),"错误",MB_ICONERROR);
      return;  
   }
	EmptyClipboard();//清空剪切板,让当前窗口进程拥有剪切板
	HANDLE hClip;
	hClip=GlobalAlloc(GMEM_MOVEABLE,m_Result.GetLength()+1);//分配内存对象返回地址(该函数是系统从全局堆中分配内存)
	char *pBuf;
	pBuf=(char *)GlobalLock(hClip);//锁定全局内存中指定的内存块，并返回一个地址值，令其指向内存块的起始处
	strcpy(pBuf,m_Result);//将Str对象中的数据Copy到内存空间中
	GlobalUnlock(hClip);//解锁全局内存块
    SetClipboardData(CF_TEXT,hClip);//设置剪贴板数据
    CloseClipboard();//关闭
}

void CCalculDlg::OnEditPaste() 
{
	// TODO: Add your command handler code here
	if(IsClipboardFormatAvailable(CF_TEXT))//获取剪贴板里的格式是否可以处理  
	{  
	   if(OpenClipboard())  
	   {  
	    HANDLE hClip;  
	    char *pBuf;  
	    hClip=GetClipboardData(CF_TEXT); //检索从指定格式剪贴板数据,并返回一个剪贴板对象句柄  
	    pBuf=(char *)GlobalLock(hClip);//锁定全局内存中指定的内存块 并返回一个地址值,并返回数据指针头地址  
	    GlobalUnlock(hClip);           //解锁  
	    SetDlgItemText(IDC_EDIT1,pBuf);  
	    CloseClipboard();  
	   }  
	}  
	e = 0;
	m_Result = "";
}
